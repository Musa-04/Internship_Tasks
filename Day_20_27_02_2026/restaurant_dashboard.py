import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import seaborn as sns


df = sns.load_dataset("tips")


df.drop_duplicates(inplace=True)

# No null values in this dataset
# But checking explicitly
df.fillna(0, inplace=True)

# ==========================================
# 3️⃣ FEATURE ENGINEERING
# ==========================================

df["tip_pct"] = (df["tip"] / df["total_bill"]) * 100

# ==========================================
# 4️⃣ KPI CALCULATIONS
# ==========================================

total_revenue = round(df["total_bill"].sum(), 2)
total_tips = round(df["tip"].sum(), 2)
avg_tip_pct = round(df["tip_pct"].mean(), 2)
avg_bill = round(df["total_bill"].mean(), 2)

peak_revenue_day = df.groupby("day")["total_bill"].sum().idxmax()
revenue_by_time = df.groupby("time")["total_bill"].sum()
smoker_revenue = df.groupby("smoker")["total_bill"].sum()

# ==========================================
# 5️⃣ CHARTS
# ==========================================

# Revenue by Day
rev_day_chart = px.bar(
    df,
    x="day",
    y="total_bill",
    color="day",
    title="Revenue by Day",
    labels={"total_bill": "Revenue"},
    barmode="group",
)

rev_day_chart.update_traces(selector=dict(type="bar"), showlegend=False)
rev_day_chart.update_layout(yaxis_title="Total Revenue")

# Revenue by Time
rev_time_chart = px.bar(
    df,
    x="time",
    y="total_bill",
    color="time",
    title="Revenue by Time (Lunch vs Dinner)",
)

# Tip % Distribution
tip_dist_chart = px.histogram(
    df,
    x="tip_pct",
    nbins=20,
    title="Tip % Distribution",
)

# Total Bill vs Tip
bill_tip_chart = px.scatter(
    df,
    x="total_bill",
    y="tip",
    color="time",
    size="size",
    title="Total Bill vs Tip (Relationship Analysis)",
)

# Revenue by Gender
gender_chart = px.bar(
    df,
    x="sex",
    y="total_bill",
    color="sex",
    title="Revenue by Gender",
)

# Revenue by Party Size
party_chart = px.box(
    df,
    x="size",
    y="total_bill",
    title="Revenue by Party Size (Outlier Detection)",
)

# Day + Time Revenue
multi_chart = px.bar(
    df,
    x="day",
    y="total_bill",
    color="time",
    title="Day + Time Revenue Comparison",
    barmode="group",
)

# ==========================================
# 6️⃣ DASH APP LAYOUT
# ==========================================

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("🍽️ Restaurant Business Analytics Dashboard",
            style={"textAlign": "center"}),

    # ================= KPI SECTION =================

    html.Div([
        html.Div([
            html.H3("Total Revenue"),
            html.H2(f"${total_revenue}")
        ], className="kpi"),

        html.Div([
            html.H3("Total Tips"),
            html.H2(f"${total_tips}")
        ], className="kpi"),

        html.Div([
            html.H3("Average Tip %"),
            html.H2(f"{avg_tip_pct}%")
        ], className="kpi"),

        html.Div([
            html.H3("Average Bill"),
            html.H2(f"${avg_bill}")
        ], className="kpi"),

        html.Div([
            html.H3("Peak Revenue Day"),
            html.H2(peak_revenue_day)
        ], className="kpi"),

    ], style={"display": "flex", "justifyContent": "space-around"}),

    html.Hr(),

    # ================= CHARTS =================

    dcc.Graph(figure=rev_day_chart),
    dcc.Graph(figure=rev_time_chart),
    dcc.Graph(figure=tip_dist_chart),
    dcc.Graph(figure=bill_tip_chart),
    dcc.Graph(figure=gender_chart),
    dcc.Graph(figure=party_chart),
    dcc.Graph(figure=multi_chart),

])


if __name__ == "__main__":
    app.run(debug=True)