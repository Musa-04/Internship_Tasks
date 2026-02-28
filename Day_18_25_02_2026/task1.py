import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# -----------------------------
# Generate Sample Stock Data
# -----------------------------
np.random.seed(42)

dates = pd.date_range("2024-01-01", "2024-12-31")
companies = ["TCS", "INFOSYS", "WIPRO"]

data = []

for company in companies:
    price = 1000 + np.random.randint(0, 200)
    for date in dates:
        price += np.random.normal(0, 5)
        volume = np.random.randint(1000, 8000)

        data.append({
            "Date": date,
            "Company": company,
            "Price": round(price, 2),
            "Volume": volume
        })

df = pd.DataFrame(data)

# -----------------------------
# Create Dash App
# -----------------------------
app = dash.Dash(__name__)
app.title = "Stock Dashboard"

# -----------------------------
# Layout
# -----------------------------
app.layout = html.Div([

    html.H1("📊 Stock Market Analytics Dashboard",
            style={"textAlign": "center"}),

    html.Div([

        dcc.Dropdown(
            id="company-dropdown",
            options=[{"label": c, "value": c} for c in df["Company"].unique()],
            value="TCS",
            clearable=False,
            style={"width": "40%", "display": "inline-block"}
        ),

        dcc.DatePickerRange(
            id="date-picker",
            start_date=df["Date"].min(),
            end_date=df["Date"].max(),
            style={"marginLeft": "5%"}
        )

    ], style={"textAlign": "center"}),

    html.Br(),

    html.Div(id="kpi-card",
             style={
                 "padding": "15px",
                 "backgroundColor": "#f2f2f2",
                 "width": "30%",
                 "margin": "auto",
                 "textAlign": "center",
                 "fontSize": "20px",
                 "borderRadius": "10px"
             }),

    html.Br(),

    dcc.Graph(id="price-chart"),
    dcc.Graph(id="volume-chart")

])

# -----------------------------
# Callback
# -----------------------------
@app.callback(
    Output("price-chart", "figure"),
    Output("volume-chart", "figure"),
    Output("kpi-card", "children"),
    Input("company-dropdown", "value"),
    Input("date-picker", "start_date"),
    Input("date-picker", "end_date")
)
def update_dashboard(company, start_date, end_date):

    filtered = df[
        (df["Company"] == company) &
        (df["Date"] >= start_date) &
        (df["Date"] <= end_date)
    ]

    # Line Chart
    price_fig = px.line(
        filtered,
        x="Date",
        y="Price",
        title=f"{company} Stock Price Trend"
    )

    # Bar Chart
    volume_fig = px.bar(
        filtered,
        x="Date",
        y="Volume",
        title=f"{company} Trading Volume"
    )

    # KPI Calculation
    if len(filtered) > 1:
        latest = filtered.iloc[-1]["Price"]
        previous = filtered.iloc[-2]["Price"]
        change = ((latest - previous) / previous) * 100
    else:
        change = 0

    kpi_text = f"Daily Change: {change:.2f}%"

    return price_fig, volume_fig, kpi_text


if __name__ == "__main__":
    app.run(debug=True)