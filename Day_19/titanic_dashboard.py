import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import numpy as np
import seaborn as sns

# ===============================
# LOAD DATA DIRECTLY FROM PYTHON
# ===============================

df = sns.load_dataset("titanic")

# ===============================
# DATA CLEANING
# ===============================

df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
df['fare'].fillna(df['fare'].median(), inplace=True)

# Create Age Groups
def age_group(age):
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

df["Age_Group"] = df["age"].apply(age_group)

# Family Size
df["Family_Size"] = df["sibsp"] + df["parch"] + 1

# ===============================
# KPI CALCULATIONS
# ===============================

total_passengers = len(df)
total_survivors = df["survived"].sum()
total_non_survivors = total_passengers - total_survivors
overall_survival_rate = round((total_survivors / total_passengers) * 100, 2)

gender_survival = df.groupby("sex")["survived"].mean() * 100
age_survival = df.groupby("Age_Group")["survived"].mean() * 100
class_survival = df.groupby("pclass")["survived"].mean() * 100
fare_avg = df.groupby("survived")["fare"].mean()
embark_survival = df.groupby("embarked")["survived"].mean() * 100
family_survival = df.groupby("Family_Size")["survived"].mean() * 100

# ===============================
# CHARTS
# ===============================

# 1 Survival Distribution
donut_chart = px.pie(
    df,
    names="survived",
    hole=0.4,
    title="Survival Distribution (0 = No, 1 = Yes)"
)

# 2 Survival by Gender
gender_chart = px.bar(
    gender_survival,
    labels={"value": "Survival Rate (%)", "index": "Gender"},
    title="Survival Rate by Gender"
)

# 3 Survival by Passenger Class
class_chart = px.histogram(
    df,
    x="pclass",
    color="survived",
    barmode="stack",
    title="Survival by Passenger Class"
)

# 4 Age Distribution by Survival
age_chart = px.histogram(
    df,
    x="age",
    color="survived",
    nbins=30,
    title="Age Distribution by Survival"
)

# 5 Fare vs Survival
fare_chart = px.box(
    df,
    x="survived",
    y="fare",
    title="Fare Distribution by Survival"
)

# 6 Survival by Embarkation Port
embark_chart = px.bar(
    embark_survival,
    labels={"value": "Survival Rate (%)", "index": "Embarkation Port"},
    title="Survival Rate by Embarkation Port"
)

# 7 Family Size Impact
family_chart = px.bar(
    family_survival,
    labels={"value": "Survival Rate (%)", "Family_Size": "Family Size"},
    title="Survival Rate by Family Size"
)

# ===============================
# DASH APP
# ===============================

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("🚢 Titanic Survival Analytics Dashboard",
            style={'textAlign': 'center'}),

    # ================= KPIs =================
    html.Div([
        html.Div([
            html.H3("Total Passengers"),
            html.H2(total_passengers)
        ], style={'padding':20}),

        html.Div([
            html.H3("Total Survivors"),
            html.H2(total_survivors)
        ], style={'padding':20}),

        html.Div([
            html.H3("Total Non-Survivors"),
            html.H2(total_non_survivors)
        ], style={'padding':20}),

        html.Div([
            html.H3("Overall Survival Rate"),
            html.H2(f"{overall_survival_rate}%")
        ], style={'padding':20}),

    ], style={'display': 'flex', 'justifyContent': 'space-around'}),

    html.Hr(),

    dcc.Graph(figure=donut_chart),
    dcc.Graph(figure=gender_chart),
    dcc.Graph(figure=class_chart),
    dcc.Graph(figure=age_chart),
    dcc.Graph(figure=fare_chart),
    dcc.Graph(figure=embark_chart),
    dcc.Graph(figure=family_chart),

])

# ===============================
# RUN
# ===============================

if __name__ == "__main__":
    app.run(debug=True)