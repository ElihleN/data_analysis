# Global Online Store Analytics

This project demonstrates an end-to-end data analysis workflow for a global retail sales dataset. The aim is to transform raw transactional data into reliable, analysis-ready tables and an interactive dashboard that supports business performance review.

The project combines SQL-based data preparation with Python dashboard development. It is documented as a reproducible analytics workflow so that another analyst can understand the data pipeline, reproduce the analysis, and extend the dashboard.

---

## Project Objectives

The main objectives of this project are to:

- Clean and structure raw sales data imported into MySQL
- Convert imported text fields into appropriate analytical data types
- Check data quality issues such as missing values and duplicate records
- Build reusable SQL views for business analysis
- Create analysis-ready summary tables for dashboarding
- Connect Python to MySQL using environment variables
- Build an interactive dashboard for exploring sales, profit, customers, countries, and segments

---

## Business Questions

This project is designed around practical business questions, including:

- Which product categories generate the highest sales and profit?
- Which regions and countries contribute most to business performance?
- How do sales and profit change over time?
- Which customer segments are most valuable?
- Which customers generate the highest sales?
- Which products or sub-categories may be associated with losses?
- How do shipping modes relate to order volume, sales, profit, and shipping cost?

---

## Workflow Overview

```text
Raw imported table
        ↓
SQL cleaning and type conversion
        ↓
Data quality checks
        ↓
Cleaned analytical table
        ↓
Reusable SQL views and summary tables
        ↓
Python database connection
        ↓
Interactive Dash dashboard
```

---

## Files in This Project

| File | Purpose |
|---|---|
| `data_cleaning.sql` | Creates the database workflow, renames the raw imported table, converts fields into analytical data types, checks missing values and duplicates, creates a cleaned table, and performs exploratory SQL analysis. |
| `eda_views.sql` | Creates reusable SQL views for category, region, yearly trend, monthly trend, customer, product, segment, shipping mode, and sub-category analysis. |
| `analysis_dataset.sql` | Creates analysis-ready summary tables for country-level performance, monthly sales/profit, and customer-level summaries. |
| `dash_app.py` | Builds an interactive Dash dashboard with a dropdown-based chart selector and KPI cards. |
| `dash_v2.py` | Provides a cleaner tab-based dashboard version with pre-built Plotly figures and KPI cards. |

---

## Data Preparation Summary

The SQL workflow prepares the raw imported sales table for analysis by:

- Creating and selecting the project database
- Inspecting the raw imported table
- Renaming the raw table for consistency
- Creating a typed working table
- Parsing order and shipping dates
- Converting sales, profit, discount, quantity, and shipping cost into numeric fields
- Checking missing values across major fields
- Removing the postal code field because it is mostly missing
- Identifying duplicate order-product combinations
- Creating a cleaned table that keeps one row per order-product combination
- Running sanity checks on date ranges and numeric fields

---

## Analytical Outputs

The SQL scripts generate outputs for several areas of analysis:

### Sales and Profit Performance

- Category-level sales and profit
- Region-level sales and profit
- Yearly and monthly sales/profit trends
- Country-level summary tables

### Customer Analysis

- Customer-level total sales
- Customer-level total profit
- Total number of orders per customer
- Top customers by revenue
- Loss-making customer groups

### Product and Segment Analysis

- Product profitability
- Loss-making products
- Segment-level sales, profit, and average discount
- Sub-category profitability
- Loss-making sub-categories

### Shipping Analysis

- Order volume by shipping mode
- Sales and profit by shipping mode
- Average shipping cost by shipping mode

---

## Dashboard Summary

The Python dashboard connects to MySQL and visualizes the SQL outputs using Dash and Plotly.

The dashboard includes:

- KPI cards for total sales, total profit, total orders, and number of customers
- Monthly sales trend chart
- Sales by category
- Sales by region
- Sales by segment
- Top countries by sales
- Top customers by sales

`dash_v2.py` is the recommended version for presentation because it uses a cleaner tab-based layout.

---

## Setup Instructions

### 1. Install Python dependencies

Create and activate a Python environment, then install the required packages:

```bash
pip install pandas sqlalchemy pymysql dash plotly python-dotenv
```

### 2. Prepare the MySQL database

Import the raw Global Superstore dataset into MySQL first. Then run the SQL files in this order:

```text
1. data_cleaning.sql
2. eda_views.sql
3. analysis_dataset.sql
```

The dashboard expects the SQL views and summary tables to already exist in the database.

### 3. Create a `.env` file

Create a `.env` file inside the project folder or working directory with the following variables:

```env
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_NAME=global_superstoreDB
```

Do not commit real passwords or private credentials to GitHub.

### 4. Run the dashboard

Run the preferred dashboard version:

```bash
python dash_v2.py
```

Then open the local Dash URL displayed in the terminal.

---

## Technical Skills Demonstrated

This project demonstrates:

- SQL data cleaning and transformation
- MySQL database preparation
- Data type conversion and date parsing
- Missing-value and duplicate-record checks
- Analytical SQL aggregation
- Creation of reusable SQL views
- Creation of dashboard-ready summary tables
- Python-to-MySQL connection using SQLAlchemy
- Secure configuration with environment variables
- Interactive dashboard development with Dash and Plotly
- Documentation of a reproducible analytics workflow

---

## Notes and Assumptions

- The raw dataset is assumed to be imported into MySQL before the SQL scripts are run.
- The SQL scripts assume a MySQL environment.
- The dashboard assumes that the SQL views and summary tables have already been created.
- The `.env` file is required for database credentials.
- The project focuses on data analysis and dashboarding, not predictive modelling.

---

## Suggested Future Improvements

Possible future improvements include:

- Add dashboard screenshots to the README
- Add a sample insights section with final business observations
- Add a `requirements.txt` file
- Add a database schema diagram
- Add error-handling around the dashboard database connection
- Add a short notebook that explains the analysis visually step by step

---

## Project Status

This project is suitable as a portfolio case study for data analysis, business intelligence, analytics engineering foundations, and technical documentation practice.
