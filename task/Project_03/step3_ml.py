import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import joblib, os, warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("data/ecommerce_clean.csv")
os.makedirs("data/plots", exist_ok=True)
os.makedirs("model", exist_ok=True)

# ═══════════════════════════════════════════════════
# PART A — CUSTOMER SEGMENTATION (KMeans Clustering)
# ═══════════════════════════════════════════════════

print("=" * 50)
print(" PART A: Customer Segmentation")
print("=" * 50)

# Build customer profile
customer_df = df.groupby('CustomerID').agg(
    TotalSpent    = ('TotalAmount', 'sum'),
    TotalOrders   = ('CustomerID', 'count'),
    AvgOrderValue = ('TotalAmount', 'mean'),
    AvgRating     = ('Rating', 'mean'),
    TotalQuantity = ('Quantity', 'sum')
).reset_index()

print(f"\nCustomer profiles built: {customer_df.shape[0]} customers")
print(customer_df.head())

# Scale features
features = ['TotalSpent', 'TotalOrders', 'AvgOrderValue', 'AvgRating', 'TotalQuantity']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(customer_df[features])

# Find best K using Elbow method
inertias, sil_scores = [], []
K_range = range(2, 9)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X_scaled, km.labels_))

# Plot Elbow curve
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(K_range, inertias, marker='o', color='#3498db')
axes[0].set_title('Elbow Method')
axes[0].set_xlabel('Number of Clusters (K)')
axes[0].set_ylabel('Inertia')
axes[1].plot(K_range, sil_scores, marker='o', color='#e74c3c')
axes[1].set_title('Silhouette Scores')
axes[1].set_xlabel('Number of Clusters (K)')
axes[1].set_ylabel('Score')
plt.tight_layout()
plt.savefig("data/plots/plot9_elbow_silhouette.png")
plt.show()
print("Plot 9 saved!")

# Train final KMeans with K=4
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
customer_df['Segment'] = kmeans.fit_predict(X_scaled)

# Label segments meaningfully
segment_summary = customer_df.groupby('Segment')[features].mean()
print(f"\nSegment Summary:\n{segment_summary}")

segment_labels = {
    customer_df.groupby('Segment')['TotalSpent'].mean().idxmax(): 'High Spender',
    customer_df.groupby('Segment')['TotalOrders'].mean().idxmax(): 'Frequent Buyer',
    customer_df.groupby('Segment')['AvgRating'].mean().idxmax(): 'Happy Customer',
}
customer_df['SegmentName'] = customer_df['Segment'].map(
    lambda x: segment_labels.get(x, 'Regular Customer'))

print(f"\nSegment Distribution:\n{customer_df['SegmentName'].value_counts()}")

# Plot segments using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
customer_df['PCA1'] = X_pca[:, 0]
customer_df['PCA2'] = X_pca[:, 1]

plt.figure(figsize=(8, 5))
colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12']
for i, seg in enumerate(customer_df['SegmentName'].unique()):
    mask = customer_df['SegmentName'] == seg
    plt.scatter(customer_df.loc[mask, 'PCA1'],
                customer_df.loc[mask, 'PCA2'],
                label=seg, alpha=0.6, color=colors[i], s=30)
plt.title('Customer Segments (PCA View)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.tight_layout()
plt.savefig("data/plots/plot10_customer_segments.png")
plt.show()
print("Plot 10 saved!")

# Segment stats bar chart
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, col, title in zip(axes,
    ['TotalSpent', 'TotalOrders', 'AvgRating'],
    ['Avg Total Spent', 'Avg Orders', 'Avg Rating']):
    seg_avg = customer_df.groupby('SegmentName')[col].mean().sort_values(ascending=False)
    sns.barplot(x=seg_avg.index, y=seg_avg.values, palette='viridis', ax=ax)
    ax.set_title(title)
    ax.set_xlabel('')
    ax.tick_params(axis='x', rotation=15)
plt.tight_layout()
plt.savefig("data/plots/plot11_segment_stats.png")
plt.show()
print("Plot 11 saved!")

# ═══════════════════════════════════════════════════
# PART B — RECOMMENDATION SYSTEM
# ═══════════════════════════════════════════════════

print("\n" + "=" * 50)
print(" PART B: Recommendation System")
print("=" * 50)

# Build user-product rating matrix
rating_matrix = df.pivot_table(
    index='CustomerID',
    columns='Product',
    values='Rating',
    aggfunc='mean'
).fillna(0)

print(f"\nRating matrix shape: {rating_matrix.shape}")

def get_recommendations(customer_id, rating_matrix, top_n=5):
    """Content-based: recommend products the customer hasn't bought yet,
       ranked by what similar customers liked."""
    if customer_id not in rating_matrix.index:
        return []

    # Cosine similarity between this customer and all others
    from sklearn.metrics.pairwise import cosine_similarity
    sim_matrix = cosine_similarity(rating_matrix)
    sim_df = pd.DataFrame(sim_matrix,
                          index=rating_matrix.index,
                          columns=rating_matrix.index)

    # Get top 10 similar customers
    similar_customers = sim_df[customer_id].sort_values(ascending=False)[1:11].index

    # Products this customer already bought
    already_bought = set(df[df['CustomerID'] == customer_id]['Product'].unique())

    # Score products from similar customers
    scores = {}
    for sim_cust in similar_customers:
        sim_score = sim_df[customer_id][sim_cust]
        cust_products = df[df['CustomerID'] == sim_cust]
        for _, row in cust_products.iterrows():
            product = row['Product']
            if product not in already_bought:
                scores[product] = scores.get(product, 0) + sim_score * row['Rating']

    recommended = sorted(scores, key=scores.get, reverse=True)[:top_n]
    return recommended

# Test recommendations
sample_customer = df['CustomerID'].iloc[0]
recs = get_recommendations(sample_customer, rating_matrix)
print(f"\nSample recommendations for Customer {sample_customer}:")
for i, r in enumerate(recs, 1):
    print(f"  {i}. {r}")

# ── Save everything ──────────────────────────────────────────────────────
customer_df.to_csv("data/customer_segments.csv", index=False)
joblib.dump(kmeans,  "model/kmeans_model.pkl")
joblib.dump(scaler,  "model/scaler.pkl")
joblib.dump(rating_matrix, "model/rating_matrix.pkl")
joblib.dump(features, "model/features.pkl")

print("\n✅ Customer segments saved to data/customer_segments.csv")
print("✅ KMeans model saved to model/kmeans_model.pkl")
print("✅ Rating matrix saved to model/rating_matrix.pkl")
print("✅ Ready for Streamlit!")