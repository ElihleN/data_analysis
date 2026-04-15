
-- Exploratory Analysis Views --

USE global_superstoreDB;

CREATE OR REPLACE VIEW vw_category_performance AS
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_sorted
GROUP BY category;

CREATE OR REPLACE VIEW vw_region_performance AS
SELECT
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_sorted
GROUP BY region;

CREATE OR REPLACE VIEW vw_yearly_sales_trend AS
SELECT
    YEAR(order_date) AS year,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_sorted
GROUP BY YEAR(order_date);

CREATE OR REPLACE VIEW vw_monthly_sales_trend AS
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_sorted
GROUP BY YEAR(order_date), MONTH(order_date);

CREATE OR REPLACE VIEW vw_top_customers AS
SELECT
    customer_id,
    customer_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(order_id) AS total_orders
FROM g_superstore_sorted
GROUP BY customer_id, customer_name;

CREATE OR REPLACE VIEW vw_loss_making_customers AS
SELECT
    customer_id,
    customer_name,
    SUM(profit) AS total_profit
FROM g_superstore_sorted
GROUP BY customer_id, customer_name;


## -- Product analysis
-- top 10 products by profit
CREATE OR REPLACE VIEW vw_product_profitability AS
SELECT
    product_id,
    product_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_sorted
GROUP BY product_id, product_name
ORDER BY total_profit DESC
LIMIT 10;

-- top 10 loss-making products
SELECT
product_id,
product_name,
SUM(sales) AS total_sales,
SUM(profit) AS total_profit
FROM g_superstore_sorted
GROUP BY product_id, product_name
ORDER BY total_profit ASC
LIMIT 10;


-- ##segment performance analysis
-- sales and profit by customer segment
CREATE OR REPLACE VIEW vw_segment_performance AS
SELECT
    segment,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    AVG(discount) AS avg_discount
FROM g_superstore_sorted
GROUP BY segment;


-- ## shipping mode performance
-- shipping mode efficiency
CREATE OR REPLACE VIEW vw_ship_mode_performance AS
SELECT
    ship_mode,
    COUNT(order_id) AS total_orders,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    AVG(shipping_cost) AS avg_shipping_cost
FROM g_superstore_sorted
GROUP BY ship_mode;

-- ####subcategory profitability
-- sub-category performance 
CREATE OR REPLACE VIEW vw_subcategory_performance AS
SELECT
    sub_category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM g_superstore_sorted
GROUP BY sub_category;

-- loss-making sub-categories
CREATE OR REPLACE VIEW vw_loss_making_subcategories AS
SELECT
    sub_category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM g_superstore_sorted
GROUP BY sub_category
HAVING SUM(profit) < 0;