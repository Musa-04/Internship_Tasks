import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics.pairwise import cosine_similarity

# ── Page Config ───────────────────────────────────────────────────────────
st.set_page_config(
    page_title="E-Commerce Dashboard",
    page_icon="🛒",
    layout="wide"
)

# ── Load Data & Models ────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df       = pd.read_csv("data/ecommerce_clean.csv")
    segments = pd.read_csv("data/customer_segments.csv")
    return df, segments

@st.cache_resource
def load_models():
    kmeans       = joblib.load("model/kmeans_model.pkl")
    scaler       = joblib.load("model/scaler.pkl")
    rating_matrix= joblib.load("model/rating_matrix.pkl")
    features     = joblib.load("model/features.pkl")
    return kmeans, scaler, rating_matrix, features

df, segments     = load_data()
kmeans, scaler, rating_matrix, features = load_models()

# ── Sidebar ───────────────────────────────────────────────────────────────
st.sidebar.image("https://img.icons8.com/fluency/96/shopping-cart.png", width=80)
st.sidebar.title("🛒 E-Commerce Analytics")
page = st.sidebar.radio("Navigate", [
    "📊 Overview",
    "👥 Customer Segments",
    "🎯 Recommendations",
    "🔍 Customer Lookup"
])

# ════════════════════════════════════════════════════
# PAGE 1 — OVERVIEW
# ════════════════════════════════════════════════════
if page == "📊 Overview":
    st.title("📊 E-Commerce Overview")

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue",    f"₹{df['TotalAmount'].sum():,.0f}")
    col2.metric("Total Orders",     f"{len(df):,}")
    col3.metric("Unique Customers", f"{df['CustomerID'].nunique():,}")
    col4.metric("Avg Rating",       f"{df['Rating'].mean():.2f} ⭐")

    st.markdown("---")

    # Sales by Category
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Sales by Category")
        cat_sales = df.groupby('Category')['TotalAmount'].sum().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(6, 3))
        sns.barplot(x=cat_sales.index, y=cat_sales.values, palette='viridis', ax=ax)
        ax.set_ylabel("Revenue (₹)")
        ax.set_xlabel("")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("Payment Methods")
        fig, ax = plt.subplots(figsize=(6, 3))
        df['PaymentMethod'].value_counts().plot.pie(
            autopct='%1.1f%%', ax=ax,
            colors=['#3498db','#2ecc71','#e74c3c','#f39c12'],
            startangle=90)
        ax.set_ylabel("")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    # Monthly Trend
    st.subheader("Monthly Sales Trend")
    monthly = df.groupby('Month')['TotalAmount'].sum()
    fig, ax = plt.subplots(figsize=(10, 3))
    sns.lineplot(x=monthly.index, y=monthly.values, marker='o', color='#3498db', ax=ax)
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue (₹)")
    ax.set_xticks(range(1, 13))
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # Top Products
    st.subheader("Top 10 Products by Revenue")
    top_p = df.groupby('Product')['TotalAmount'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 3))
    sns.barplot(x=top_p.values, y=top_p.index, palette='magma', ax=ax)
    ax.set_xlabel("Revenue (₹)")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# ════════════════════════════════════════════════════
# PAGE 2 — CUSTOMER SEGMENTS
# ════════════════════════════════════════════════════
elif page == "👥 Customer Segments":
    st.title("👥 Customer Segmentation")

    # Segment counts
    seg_counts = segments['SegmentName'].value_counts()
    col1, col2, col3, col4 = st.columns(4)
    colors_map = {
        'High Spender':     '🔴',
        'Frequent Buyer':   '🟢',
        'Happy Customer':   '🔵',
        'Regular Customer': '🟡'
    }
    for col, (seg, count) in zip([col1,col2,col3,col4], seg_counts.items()):
        col.metric(f"{colors_map.get(seg,'⚪')} {seg}", f"{count} customers")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Segment Distribution")
        fig, ax = plt.subplots(figsize=(5, 4))
        seg_counts.plot.pie(autopct='%1.1f%%', ax=ax, startangle=90,
                            colors=['#e74c3c','#2ecc71','#3498db','#f39c12'])
        ax.set_ylabel("")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("Avg Spend by Segment")
        fig, ax = plt.subplots(figsize=(5, 4))
        seg_spend = segments.groupby('SegmentName')['TotalSpent'].mean().sort_values(ascending=False)
        sns.barplot(x=seg_spend.index, y=seg_spend.values, palette='viridis', ax=ax)
        ax.set_ylabel("Avg Total Spent (₹)")
        ax.set_xlabel("")
        ax.tick_params(axis='x', rotation=15)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    st.subheader("Segment Details")
    summary = segments.groupby('SegmentName').agg(
        Customers   = ('CustomerID', 'count'),
        Avg_Spent   = ('TotalSpent', 'mean'),
        Avg_Orders  = ('TotalOrders', 'mean'),
        Avg_Rating  = ('AvgRating', 'mean')
    ).round(2)
    st.dataframe(summary, use_container_width=True)

# ════════════════════════════════════════════════════
# PAGE 3 — RECOMMENDATIONS
# ════════════════════════════════════════════════════
elif page == "🎯 Recommendations":
    st.title("🎯 Product Recommendations")

    all_customers = sorted(df['CustomerID'].unique())
    customer_id   = st.selectbox("Select a Customer ID", all_customers)
    top_n         = st.slider("Number of Recommendations", 3, 10, 5)

    if st.button("Get Recommendations 🚀"):
        already_bought = df[df['CustomerID'] == customer_id]['Product'].unique()

        st.subheader(f"Products already bought by Customer {customer_id}")
        cols = st.columns(len(already_bought))
        for col, product in zip(cols, already_bought):
            col.success(f"✅ {product}")

        # Compute recommendations
        if customer_id in rating_matrix.index:
            sim_matrix = cosine_similarity(rating_matrix)
            sim_df     = pd.DataFrame(sim_matrix,
                                      index=rating_matrix.index,
                                      columns=rating_matrix.index)
            similar_customers = sim_df[customer_id].sort_values(ascending=False)[1:11].index
            already_set = set(already_bought)
            scores = {}
            for sim_cust in similar_customers:
                sim_score  = sim_df[customer_id][sim_cust]
                cust_prods = df[df['CustomerID'] == sim_cust]
                for _, row in cust_prods.iterrows():
                    p = row['Product']
                    if p not in already_set:
                        scores[p] = scores.get(p, 0) + sim_score * row['Rating']

            recommended = sorted(scores, key=scores.get, reverse=True)[:top_n]

            st.subheader(f"🎯 Top {top_n} Recommendations")
            for i, product in enumerate(recommended, 1):
                cat = df[df['Product'] == product]['Category'].iloc[0]
                avg_rating = df[df['Product'] == product]['Rating'].mean()
                avg_price  = df[df['Product'] == product]['Price'].mean()
                col1, col2, col3, col4 = st.columns([1, 3, 2, 2])
                col1.write(f"**#{i}**")
                col2.write(f"🛍️ **{product}**")
                col3.write(f"📦 {cat}")
                col4.write(f"⭐ {avg_rating:.1f} | ₹{avg_price:,.0f}")
        else:
            st.warning("Customer not found in rating matrix.")

# ════════════════════════════════════════════════════
# PAGE 4 — CUSTOMER LOOKUP
# ════════════════════════════════════════════════════
elif page == "🔍 Customer Lookup":
    st.title("🔍 Customer Lookup")

    customer_id = st.selectbox("Select Customer ID", sorted(df['CustomerID'].unique()))

    cust_data   = df[df['CustomerID'] == customer_id]
    cust_seg    = segments[segments['CustomerID'] == customer_id]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Spent",  f"₹{cust_data['TotalAmount'].sum():,.0f}")
    col2.metric("Total Orders", f"{len(cust_data)}")
    col3.metric("Avg Rating",   f"{cust_data['Rating'].mean():.2f} ⭐")
    if not cust_seg.empty:
        col4.metric("Segment", cust_seg['SegmentName'].values[0])

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Products Purchased")
        prod_counts = cust_data['Product'].value_counts()
        fig, ax = plt.subplots(figsize=(5, 3))
        sns.barplot(x=prod_counts.values, y=prod_counts.index, palette='Blues_d', ax=ax)
        ax.set_xlabel("Times Purchased")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("Spending by Category")
        cat_spend = cust_data.groupby('Category')['TotalAmount'].sum()
        fig, ax = plt.subplots(figsize=(5, 3))
        cat_spend.plot.pie(autopct='%1.1f%%', ax=ax, startangle=90)
        ax.set_ylabel("")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    st.subheader("Purchase History")
    st.dataframe(
        cust_data[['Date','Product','Category','Quantity','Price','Rating','PaymentMethod']]
        .sort_values('Date', ascending=False),
        use_container_width=True
    )