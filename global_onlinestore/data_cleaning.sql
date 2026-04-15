
--  database
CREATE DATABASE IF NOT EXISTS global_superstoreDB;
USE global_superstoreDB;

-- Inspect raw imported table
SELECT *
FROM glob_superstore_data
LIMIT 10;

-- Rename raw table for consistency
RENAME TABLE glob_superstore_data TO g_superstore;

SELECT *
FROM g_superstore
LIMIT 10;

DESCRIBE g_superstore;

-- Create typed working table
--    Convert text-heavy imported columns into suitable data types
DROP TABLE IF EXISTS g_superstore_typed;

CREATE TABLE g_superstore_typed AS
SELECT
    CAST(`Row ID` AS UNSIGNED) AS row_id,
    CAST(`Order ID` AS CHAR(30)) AS order_id,
    STR_TO_DATE(`Order Date`, '%d-%m-%Y') AS order_date,
    STR_TO_DATE(`Ship Date`, '%d-%m-%Y') AS ship_date,
    `Ship Mode` AS ship_mode,
    CAST(`Customer ID` AS CHAR(30)) AS customer_id,
    `Customer Name` AS customer_name,
    `Segment` AS segment,
    `City` AS city,
    `State` AS state,
    `Country` AS country,
    CAST(`Postal Code` AS CHAR(20)) AS postal_code,
    `Market` AS market,
    `Region` AS region,
    CAST(`Product ID` AS CHAR(30)) AS product_id,
    `Category` AS category,
    `Sub-Category` AS sub_category,
    `Product Name` AS product_name,
    CAST(`Sales` AS DECIMAL(12,2)) AS sales,
    CAST(`Quantity` AS UNSIGNED) AS quantity,
    CAST(`Discount` AS DECIMAL(5,2)) AS discount,
    CAST(`Profit` AS DECIMAL(12,2)) AS profit,
    CAST(`Shipping Cost` AS DECIMAL(12,2)) AS shipping_cost,
    `Order Priority` AS order_priority
FROM g_superstore;

DESCRIBE g_superstore_typed;

SELECT *
FROM g_superstore_typed
LIMIT 10;

--  Data quality checks
-- Check missing values in raw table
SELECT
    COUNT(*) AS total_rows,
    SUM(`Row ID` IS NULL) AS row_id_nulls,
    SUM(`Order ID` IS NULL) AS order_id_nulls,
    SUM(`Order Date` IS NULL) AS order_date_nulls,
    SUM(`Ship Date` IS NULL) AS ship_date_nulls,
    SUM(`Ship Mode` IS NULL) AS ship_mode_nulls,
    SUM(`Customer ID` IS NULL) AS customer_id_nulls,
    SUM(`Customer Name` IS NULL) AS customer_name_nulls,
    SUM(`Segment` IS NULL) AS segment_nulls,
    SUM(`City` IS NULL) AS city_nulls,
    SUM(`State` IS NULL) AS state_nulls,
    SUM(`Country` IS NULL) AS country_nulls,
    SUM(`Postal Code` IS NULL) AS postal_code_nulls,
    SUM(`Market` IS NULL) AS market_nulls,
    SUM(`Region` IS NULL) AS region_nulls,
    SUM(`Product ID` IS NULL) AS product_id_nulls,
    SUM(`Category` IS NULL) AS category_nulls,
    SUM(`Sub-Category` IS NULL) AS sub_category_nulls,
    SUM(`Product Name` IS NULL) AS product_name_nulls,
    SUM(`Sales` IS NULL) AS sales_nulls,
    SUM(`Quantity` IS NULL) AS quantity_nulls,
    SUM(`Discount` IS NULL) AS discount_nulls,
    SUM(`Profit` IS NULL) AS profit_nulls,
    SUM(`Shipping Cost` IS NULL) AS shipping_cost_nulls,
    SUM(`Order Priority` IS NULL) AS order_priority_nulls
FROM g_superstore;

-- Postal code is mostly missing, so drop it from the typed table
ALTER TABLE g_superstore_typed
DROP COLUMN postal_code;

-- Duplicate checks
--  Duplicate definition used here: same order_id + product_id
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT order_id, product_id) AS unique_order_product_rows
FROM g_superstore_typed;

-- Inspect duplicate combinations
SELECT
    order_id,
    product_id,
    COUNT(*) AS duplicate_count
FROM g_superstore_typed
GROUP BY order_id, product_id
HAVING COUNT(*) > 1;

-- Remove duplicates
--    Keep the first row per order_id + product_id
DROP TABLE IF EXISTS g_superstore_cleaned;

CREATE TABLE g_superstore_cleaned AS
SELECT *
FROM (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY order_id, product_id
            ORDER BY row_id
        ) AS rn
    FROM g_superstore_typed
) t
WHERE rn = 1;

-- Optional: remove helper column
ALTER TABLE g_superstore_cleaned
DROP COLUMN rn;

SELECT COUNT(*) AS total_rows
FROM g_superstore_cleaned;

-- Sanity checks on cleaned data
SELECT
    MIN(order_date) AS min_order_date,
    MAX(order_date) AS max_order_date,
    MIN(sales) AS min_sales,
    MAX(sales) AS max_sales,
    MIN(profit) AS min_profit,
    MAX(profit) AS max_profit,
    MIN(discount) AS min_discount,
    MAX(discount) AS max_discount,
    MIN(quantity) AS min_quantity,
    MAX(quantity) AS max_quantity
FROM g_superstore_cleaned;

-- =====================================================
-- Exploratory business analysis

-- Category performance

SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_cleaned
GROUP BY category
ORDER BY total_sales DESC;

-- Regional performance
SELECT
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_cleaned
GROUP BY region
ORDER BY total_sales DESC;

-- Sales trend analysis
-- Yearly sales and profit trend
SELECT
    YEAR(order_date) AS year,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_cleaned
GROUP BY YEAR(order_date)
ORDER BY year;

-- Monthly sales and profit trend
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_cleaned
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;

-- Customer analysis

-- Top 10 customers by revenue
SELECT
    customer_id,
    customer_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(order_id) AS total_orders
FROM g_superstore_cleaned
GROUP BY customer_id, customer_name
ORDER BY total_sales DESC
LIMIT 10;

-- Top 10 loss-making customers
SELECT
    customer_id,
    customer_name,
    SUM(profit) AS total_profit
FROM g_superstore_cleaned
GROUP BY customer_id, customer_name
ORDER BY total_profit ASC
LIMIT 10;

-- Product analysis

-- Top 10 products by profit
SELECT
    product_id,
    product_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_cleaned
GROUP BY product_id, product_name
ORDER BY total_profit DESC
LIMIT 10;

-- Top 10 loss-making products
SELECT
    product_id,
    product_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_cleaned
GROUP BY product_id, product_name
ORDER BY total_profit ASC
LIMIT 10;

-- Segment analysis
SELECT
    segment,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    AVG(discount) AS avg_discount
FROM g_superstore_cleaned
GROUP BY segment
ORDER BY total_sales DESC;

-- Shipping mode analysis
SELECT
    ship_mode,
    COUNT(order_id) AS total_orders,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    AVG(shipping_cost) AS avg_shipping_cost
FROM g_superstore_cleaned
GROUP BY ship_mode
ORDER BY total_orders DESC;

-- Sub-category profitability

--  sub-category performance
SELECT
    sub_category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM g_superstore_cleaned
GROUP BY sub_category
ORDER BY total_profit DESC;

-- Loss-making sub-categories
SELECT
    sub_category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_cleaned
GROUP BY sub_category
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;

-- =====================================================

-- Analysis-ready datasets

-- Country-level summary table
DROP TABLE IF EXISTS sales_by_country;

CREATE TABLE sales_by_country AS
SELECT
    country,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    AVG(discount) AS avg_discount
FROM g_superstore_cleaned
GROUP BY country;

-- Monthly performance summary table
DROP TABLE IF EXISTS monthly_sales;

CREATE TABLE monthly_sales AS
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_cleaned
GROUP BY YEAR(order_date), MONTH(order_date);

-- Customer summary table
DROP TABLE IF EXISTS customer_summary;

CREATE TABLE customer_summary AS
SELECT
    customer_id,
    customer_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(order_id) AS total_orders
FROM g_superstore_cleaned
GROUP BY customer_id, customer_name;