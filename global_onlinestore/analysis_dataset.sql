-- ## dataset for specific analysis

USE global_superstoreDB;

-- country-level dataset
DROP TABLE IF EXISTS sales_by_country;

CREATE TABLE sales_by_country AS
SELECT
country,
SUM(sales) AS total_sales,
SUM(profit) AS total_profit,
SUM(quantity) AS total_quantity,
AVG(discount) AS avg_discount
FROM g_superstore_sorted
GROUP BY country;

-- monthly performance dataset
DROP TABLE IF EXISTS monthly_sales;

CREATE TABLE monthly_sales AS
SELECT
YEAR(order_date) AS year,
MONTH(order_date) AS month,
SUM(sales) AS total_sales,
SUM(profit) AS total_profit
FROM g_superstore_sorted
GROUP BY year, month;

-- customer lifetime value dataset
DROP TABLE IF EXISTS customer_summary;

CREATE TABLE customer_summary AS
SELECT
customer_id,
customer_name,
SUM(sales) AS total_sales,
SUM(profit) AS total_profit,
COUNT(order_id) AS total_orders
FROM g_superstore_sorted
GROUP BY customer_id, customer_name;


