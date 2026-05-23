import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# ===============================
# LOAD DATA
# ===============================

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Rename columns for clean display
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# ===============================
# KPI CALCULATIONS
# ===============================

# 1. Total Records
total_records = len(df)

# 2. Species Distribution
species_counts = df["species"].value_counts()
species_percent = (species_counts / total_records * 100).round(2)

# 3. Average Feature Values by Species
avg_features = df.groupby("species").mean().round(2)

# 4. Correlation Matrix
corr_matrix = df.drop("species", axis=1).corr().round(2)

# 5. Outlier Detection (IQR Method)
outlier_summary = {}
for col in df.columns[:-1]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    outlier_summary[col] = {
        "count": len(outliers),
        "percentage": round(len(outliers) / total_records * 100, 2)
    }

# ===============================
# DASH APP
# ===============================

app = dash.Dash(__name__)

# ===============================
# CHARTS
# ===============================

# Species Distribution
bar_species = px.bar(
    x=species_counts.index,
    y=species_counts.values,
    labels={"x": "Species", "y": "Count"},
    title="Species Distribution"
)

# Boxplots
boxplot = px.box(
    df,
    x="species",
    y=df.columns[:-1],
    title="Feature Comparison by Species",
    points="outliers"
)

# Scatter Matrix (Pair Plot)
scatter_matrix = px.scatter_matrix(
    df,
    dimensions=df.columns[:-1],
    color="species",
    title="Pair Plot (Scatter Matrix)"
)

# Correlation Heatmap
heatmap = px.imshow(
    corr_matrix,
    text_auto=True,
    color_continuous_scale="RdBu",
    title="Correlation Heatmap"
)

# ===============================
# LAYOUT
# ===============================

app.layout = html.Div([

    html.H1("🌸 Iris Dataset Analytical Dashboard",
            style={'textAlign': 'center'}),

    # KPI Section
    html.Div([
        html.Div([
            html.H3("Total Records"),
            html.H2(total_records)
        ], className="kpi"),

        html.Div([
            html.H3("Species Distribution (%)"),
            html.P(str(species_percent.to_dict()))
        ], className="kpi"),

        html.Div([
            html.H3("Outlier Summary"),
            html.P(str(outlier_summary))
        ], className="kpi"),

    ], style={'display': 'flex', 'justifyContent': 'space-around'}),

    html.Br(),

    # Charts
    dcc.Graph(figure=bar_species),
    dcc.Graph(figure=boxplot),
    dcc.Graph(figure=scatter_matrix),
    dcc.Graph(figure=heatmap),

])

# ===============================
# RUN
# ===============================

if __name__ == "__main__":
    app.run(debug=True)