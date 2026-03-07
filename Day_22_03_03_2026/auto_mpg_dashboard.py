import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="Auto MPG Dashboard",
    layout="wide"
)

st.title("Automotive Fuel Efficiency Dashboard")

# -----------------------------------
# Load Dataset
# -----------------------------------

df = sns.load_dataset("mpg")

# Data Cleaning
df = df.dropna()

origin_map = {1: "USA", 2: "Europe", 3: "Japan"}
df["origin"] = df["origin"].map(origin_map)

df["model_year"] = df["model_year"] + 1900

# -----------------------------------
# KPI Calculations
# -----------------------------------

avg_mpg = df["mpg"].mean()
max_mpg = df["mpg"].max()
min_mpg = df["mpg"].min()
total_vehicles = df.shape[0]

avg_hp = df["horsepower"].mean()

# MPG Trend
yearly_mpg = df.groupby("model_year")["mpg"].mean().reset_index()

yoy_growth = yearly_mpg["mpg"].pct_change().mean() * 100

# Origin KPIs
origin_avg_mpg = df.groupby("origin")["mpg"].mean().reset_index()

origin_vehicle_count = df.groupby("origin")["mpg"].count()

market_share = (origin_vehicle_count / total_vehicles) * 100

# Correlation Matrix
corr_matrix = df[
    ["mpg", "weight", "horsepower", "displacement", "cylinders", "acceleration"]
].corr()

# -----------------------------------
# KPI CARDS
# -----------------------------------

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average MPG", round(avg_mpg, 2))
col2.metric("YoY MPG Growth %", round(yoy_growth, 2))
col3.metric("Average Horsepower", round(avg_hp, 2))
col4.metric("Total Vehicles", total_vehicles)

# -----------------------------------
# MPG TREND LINE
# -----------------------------------

st.subheader("Fuel Efficiency Trend")

fig_trend = px.line(
    yearly_mpg,
    x="model_year",
    y="mpg",
    markers=True,
    title="Average MPG Over Years"
)

st.plotly_chart(fig_trend, width="stretch")

# -----------------------------------
# MPG BY ORIGIN
# -----------------------------------

st.subheader("Average MPG by Origin")

fig_origin = px.bar(
    origin_avg_mpg,
    x="origin",
    y="mpg",
    color="origin",
    title="Average MPG by Origin"
)

st.plotly_chart(fig_origin, width="stretch")

# -----------------------------------
# MARKET SHARE PIE
# -----------------------------------

st.subheader("Market Share by Origin")

market_df = df["origin"].value_counts().reset_index()
market_df.columns = ["origin", "count"]

fig_pie = px.pie(
    market_df,
    names="origin",
    values="count",
    title="Vehicle Distribution by Origin"
)

st.plotly_chart(fig_pie, width="stretch")

# -----------------------------------
# SCATTER PLOTS
# -----------------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("MPG vs Weight")

    fig_scatter1 = px.scatter(
        df,
        x="weight",
        y="mpg",
        color="origin",
        trendline="ols"
    )

    st.plotly_chart(fig_scatter1, width="stretch")

with col2:
    st.subheader("MPG vs Horsepower")

    fig_scatter2 = px.scatter(
        df,
        x="horsepower",
        y="mpg",
        color="origin"
    )

    st.plotly_chart(fig_scatter2, width="stretch")

# -----------------------------------
# ENGINE CYLINDER DISTRIBUTION
# -----------------------------------

st.subheader("Engine Cylinder Distribution")

cyl_df = df["cylinders"].value_counts().reset_index()
cyl_df.columns = ["cylinders", "count"]

fig_cyl = px.bar(
    cyl_df,
    x="cylinders",
    y="count",
    color="cylinders",
    title="Engine Cylinder Distribution"
)

st.plotly_chart(fig_cyl, width="stretch")

# -----------------------------------
# MPG DISTRIBUTION
# -----------------------------------

st.subheader("MPG Distribution")

fig_hist = px.histogram(
    df,
    x="mpg",
    nbins=20,
    title="MPG Distribution"
)

st.plotly_chart(fig_hist, width="stretch")

# -----------------------------------
# CORRELATION HEATMAP
# -----------------------------------

st.subheader("Correlation Matrix")

fig, ax = plt.subplots(figsize=(8,5))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)