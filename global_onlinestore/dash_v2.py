import pandas as pd
from sqlalchemy import create_engine
from dash import Dash, dcc, html
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

# Pre-build figures
fig_monthly = px.line(
    monthly_df.sort_values("year_month"),
    x="year_month",
    y="total_sales",
    title="Monthly Sales Trend"
)

fig_category = px.bar(
    category_df.sort_values("total_sales", ascending=False),
    x="category",
    y="total_sales",
    title="Sales by Category"
)

fig_region = px.bar(
    region_df.sort_values("total_sales", ascending=False),
    x="region",
    y="total_sales",
    title="Sales by Region"
)

fig_segment = px.bar(
    segment_df.sort_values("total_sales", ascending=False),
    x="segment",
    y="total_sales",
    title="Sales by Segment"
)

fig_country = px.bar(
    country_df.sort_values("total_sales", ascending=False).head(15),
    x="country",
    y="total_sales",
    title="Top 15 Countries by Sales"
)

fig_customers = px.bar(
    customer_df.sort_values("total_sales", ascending=False).head(10),
    x="customer_name",
    y="total_sales",
    title="Top 10 Customers by Sales"
)

# KPI calculations
total_sales = customer_df["total_sales"].sum()
total_profit = customer_df["total_profit"].sum()
total_orders = customer_df["total_orders"].sum()
total_customers = customer_df["customer_id"].nunique()

# App
app = Dash(__name__)
app.title = "Global Superstore Dashboard"

app.layout = html.Div(
    style={"fontFamily": "Arial", "padding": "20px"},
    children=[
        html.H1("Global Superstore Dashboard"),
        html.P("SQL-powered interactive business dashboard"),

        html.Div(
            style={"display": "flex", "gap": "20px", "flexWrap": "wrap", "marginBottom": "25px"},
            children=[
                html.Div(
                    [
                        html.H4("Total Sales"),
                        html.P(f"${total_sales:,.2f}")
                    ],
                    style={"padding": "15px", "border": "1px solid #ddd", "minWidth": "180px"}
                ),
                html.Div(
                    [
                        html.H4("Total Profit"),
                        html.P(f"${total_profit:,.2f}")
                    ],
                    style={"padding": "15px", "border": "1px solid #ddd", "minWidth": "180px"}
                ),
                html.Div(
                    [
                        html.H4("Total Orders"),
                        html.P(f"{int(total_orders):,}")
                    ],
                    style={"padding": "15px", "border": "1px solid #ddd", "minWidth": "180px"}
                ),
                html.Div(
                    [
                        html.H4("Customers"),
                        html.P(f"{total_customers:,}")
                    ],
                    style={"padding": "15px", "border": "1px solid #ddd", "minWidth": "180px"}
                ),
            ],
        ),

        dcc.Tabs([
            dcc.Tab(label="Monthly Sales", children=[
                dcc.Graph(figure=fig_monthly)
            ]),

            dcc.Tab(label="Category Performance", children=[
                dcc.Graph(figure=fig_category)
            ]),

            dcc.Tab(label="Region Performance", children=[
                dcc.Graph(figure=fig_region)
            ]),

            dcc.Tab(label="Segment Performance", children=[
                dcc.Graph(figure=fig_segment)
            ]),

            dcc.Tab(label="Country Performance", children=[
                dcc.Graph(figure=fig_country)
            ]),

            dcc.Tab(label="Top Customers", children=[
                dcc.Graph(figure=fig_customers)
            ]),
        ])
    ]
)

if __name__ == "__main__":
    app.run(debug=True)