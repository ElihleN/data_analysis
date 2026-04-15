import pandas as pd
from sqlalchemy import create_engine
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")


# Database connection
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

# Load data from MySQL views/tables
category_df = pd.read_sql("SELECT * FROM vw_category_performance", engine)
region_df = pd.read_sql("SELECT * FROM vw_region_performance", engine)
segment_df = pd.read_sql("SELECT * FROM vw_segment_performance", engine)
monthly_df = pd.read_sql("SELECT * FROM monthly_sales", engine)
country_df = pd.read_sql("SELECT * FROM sales_by_country", engine)
customer_df = pd.read_sql("SELECT * FROM customer_summary", engine)

monthly_df["year_month"] = pd.to_datetime(
    monthly_df["year"].astype(str) + "-" + monthly_df["month"].astype(str) + "-01"
)

# App
app = Dash(__name__)
app.title = "Global Superstore Dashboard"

app.layout = html.Div(
    style={"fontFamily": "Arial", "padding": "20px"},
    children=[
        html.H1("Global Superstore Dashboard"),
        html.P("Interactive SQL-powered business dashboard"),

        html.Div(
            style={"width": "300px", "marginBottom": "20px"},
            children=[
                html.Label("Select view"),
                dcc.Dropdown(
                    id="view-selector",
                    options=[
                        {"label": "Monthly Sales Trend", "value": "monthly"},
                        {"label": "Category Performance", "value": "category"},
                        {"label": "Region Performance", "value": "region"},
                        {"label": "Segment Performance", "value": "segment"},
                        {"label": "Country Performance", "value": "country"},
                        {"label": "Top Customers", "value": "customers"},
                    ],
                    value="monthly",
                    clearable=False,
                ),
            ],
        ),

        dcc.Graph(id="main-chart"),

        html.H3("Quick KPIs"),
        html.Div(
            style={"display": "flex", "gap": "20px", "flexWrap": "wrap"},
            children=[
                html.Div(
                    [
                        html.H4("Total Sales"),
                        html.P(f"${customer_df['total_sales'].sum():,.2f}")
                    ],
                    style={"padding": "15px", "border": "1px solid #ddd", "minWidth": "180px"}
                ),
                html.Div(
                    [
                        html.H4("Total Profit"),
                        html.P(f"${customer_df['total_profit'].sum():,.2f}")
                    ],
                    style={"padding": "15px", "border": "1px solid #ddd", "minWidth": "180px"}
                ),
                html.Div(
                    [
                        html.H4("Total Orders"),
                        html.P(f"{int(customer_df['total_orders'].sum()):,}")
                    ],
                    style={"padding": "15px", "border": "1px solid #ddd", "minWidth": "180px"}
                ),
                html.Div(
                    [
                        html.H4("Customers"),
                        html.P(f"{customer_df['customer_id'].nunique():,}")
                    ],
                    style={"padding": "15px", "border": "1px solid #ddd", "minWidth": "180px"}
                ),
            ],
        ),
    ],
)

# =========================
# Callback
# =========================
@app.callback(
    Output("main-chart", "figure"),
    Input("view-selector", "value")
)
def update_chart(selected_view):
    if selected_view == "monthly":
        fig = px.line(
            monthly_df.sort_values("year_month"),
            x="year_month",
            y="total_sales",
            title="Monthly Sales Trend"
        )
        fig.update_layout(xaxis_title="Month", yaxis_title="Total Sales")
        return fig

    if selected_view == "category":
        fig = px.bar(
            category_df.sort_values("total_sales", ascending=False),
            x="category",
            y="total_sales",
            title="Sales by Category"
        )
        fig.update_layout(xaxis_title="Category", yaxis_title="Total Sales")
        return fig

    if selected_view == "region":
        fig = px.bar(
            region_df.sort_values("total_sales", ascending=False),
            x="region",
            y="total_sales",
            title="Sales by Region"
        )
        fig.update_layout(xaxis_title="Region", yaxis_title="Total Sales")
        return fig

    if selected_view == "segment":
        fig = px.bar(
            segment_df.sort_values("total_sales", ascending=False),
            x="segment",
            y="total_sales",
            title="Sales by Segment"
        )
        fig.update_layout(xaxis_title="Segment", yaxis_title="Total Sales")
        return fig

    if selected_view == "country":
        fig = px.bar(
            country_df.sort_values("total_sales", ascending=False).head(15),
            x="country",
            y="total_sales",
            title="Top 15 Countries by Sales"
        )
        fig.update_layout(xaxis_title="Country", yaxis_title="Total Sales")
        return fig

    fig = px.bar(
        customer_df.sort_values("total_sales", ascending=False).head(10),
        x="customer_name",
        y="total_sales",
        title="Top 10 Customers by Sales"
    )
    fig.update_layout(xaxis_title="Customer", yaxis_title="Total Sales")
    return fig


if __name__ == "__main__":
    app.run(debug=True)


    app.layout = html.Div([
    html.H1("Global Superstore Dashboard"),

    dcc.Tabs([
        dcc.Tab(label="Monthly Sales", children=[
            dcc.Graph(
                figure=px.line(
                    monthly_df.sort_values("year_month"),
                    x="year_month",
                    y="total_sales",
                    title="Monthly Sales Trend"
                )
            )
        ]),

        dcc.Tab(label="Category Performance", children=[
            dcc.Graph(
                figure=px.bar(
                    category_df.sort_values("total_sales", ascending=False),
                    x="category",
                    y="total_sales",
                    title="Sales by Category"
                )
            )
        ]),

        dcc.Tab(label="Region Performance", children=[
            dcc.Graph(
                figure=px.bar(
                    region_df.sort_values("total_sales", ascending=False),
                    x="region",
                    y="total_sales",
                    title="Sales by Region"
                )
            )
        ]),

        dcc.Tab(label="Segment Performance", children=[
            dcc.Graph(
                figure=px.bar(
                    segment_df.sort_values("total_sales", ascending=False),
                    x="segment",
                    y="total_sales",
                    title="Sales by Segment"
                )
            )
        ])
    ])
])