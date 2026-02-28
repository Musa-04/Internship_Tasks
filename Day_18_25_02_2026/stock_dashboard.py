import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import yfinance as yf
import pandas as pd

# Create Dash App
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([

    html.H1("📊 Live Stock Dashboard", style={'textAlign': 'center'}),

    # Dropdown for stock selection
    dcc.Dropdown(
        id='stock-dropdown',
        options=[
            {'label': 'Apple', 'value': 'AAPL'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Google', 'value': 'GOOGL'},
            {'label': 'Amazon', 'value': 'AMZN'}
        ],
        value='AAPL',
        clearable=False
    ),

    html.Br(),

    # Graph
    dcc.Graph(id='stock-graph'),

    # Auto Refresh every 10 seconds
    dcc.Interval(
        id='interval-component',
        interval=10*1000,  # 10 seconds
        n_intervals=0
    )

])


# Callback with Multiple Inputs
@app.callback(
    Output('stock-graph', 'figure'),
    [Input('stock-dropdown', 'value'),
     Input('interval-component', 'n_intervals')]
)
def update_graph(stock_symbol, n):

    # Fetch limited data (3 months to handle large datasets efficiently)
    df = yf.download(stock_symbol, period="3mo", interval="1d")

    if df.empty:
        return go.Figure()

    # Create Figure
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Close'],
        mode='lines',
        name='Closing Price'
    ))

    fig.update_layout(
        title=f"{stock_symbol} Live Stock Price",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_dark"
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)