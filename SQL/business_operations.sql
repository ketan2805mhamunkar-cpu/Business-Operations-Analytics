-- ============================================================
-- BUSINESS OPERATIONS ANALYTICS PROJECT
-- SQL ANALYSIS
-- Database: business_operations.db
-- ============================================================


-- ============================================================
-- STEP 1: BASIC SQL QUERIES
-- ============================================================

-- 1. View all orders
SELECT *
FROM orders;

-- 2. Select important columns
SELECT
    order_id,
    order_date,
    customer,
    region,
    sales_rep,
    product,
    total_sale,
    status
FROM orders;

-- 3. Find completed orders
SELECT *
FROM orders
WHERE status = 'Completed';

-- 4. Highest-value orders
SELECT
    order_id,
    customer,
    sales_rep,
    total_sale
FROM orders
ORDER BY total_sale DESC
LIMIT 10;

-- 5. Total number of orders
SELECT COUNT(*) AS total_orders
FROM orders;


-- ============================================================
-- STEP 2: AGGREGATIONS
-- ============================================================

-- Total sales
SELECT
    ROUND(SUM(total_sale), 2) AS total_sales
FROM orders;

-- Average sale
SELECT
    ROUND(AVG(total_sale), 2) AS average_sale
FROM orders;

-- Minimum and maximum sale
SELECT
    MIN(total_sale) AS minimum_sale,
    MAX(total_sale) AS maximum_sale
FROM orders;

-- Sales by region
SELECT
    region,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(total_sale), 2) AS total_sales
FROM orders
GROUP BY region
ORDER BY total_sales DESC;

-- Sales by status
SELECT
    status,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(total_sale), 2) AS total_sales
FROM orders
GROUP BY status
ORDER BY total_sales DESC;


-- ============================================================
-- STEP 3: CASE WHEN & BUSINESS KPIs
-- ============================================================

-- Categorize orders by sales value
SELECT
    order_id,
    total_sale,
    CASE
        WHEN total_sale >= 500 THEN 'High'
        WHEN total_sale >= 250 THEN 'Medium'
        ELSE 'Low'
    END AS sale_category
FROM orders;

-- Completed vs non-completed orders
SELECT
    CASE
        WHEN status = 'Completed' THEN 'Completed'
        ELSE 'Non-Completed'
    END AS order_group,
    COUNT(*) AS order_count
FROM orders
GROUP BY order_group;

-- Overall completion rate
SELECT
    ROUND(
        100.0 *
        SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS completion_rate
FROM orders;

-- Return rate
SELECT
    ROUND(
        100.0 *
        SUM(CASE WHEN status = 'Returned' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS return_rate
FROM orders;


-- ============================================================
-- STEP 4: DATE ANALYSIS
-- ============================================================

-- Orders by date
SELECT
    order_date,
    COUNT(*) AS order_count,
    ROUND(SUM(total_sale), 2) AS daily_sales
FROM orders
GROUP BY order_date
ORDER BY order_date;

-- Monthly sales
SELECT
    strftime('%Y-%m', order_date) AS month,
    COUNT(*) AS total_orders,
    ROUND(SUM(total_sale), 2) AS total_sales
FROM orders
GROUP BY month
ORDER BY month;

-- Highest-sales day
SELECT
    order_date,
    ROUND(SUM(total_sale), 2) AS daily_sales
FROM orders
GROUP BY order_date
ORDER BY daily_sales DESC
LIMIT 1;

-- Lowest-sales day
SELECT
    order_date,
    ROUND(SUM(total_sale), 2) AS daily_sales
FROM orders
GROUP BY order_date
ORDER BY daily_sales ASC
LIMIT 1;


-- ============================================================
-- STEP 5: JOIN
-- ============================================================

-- Sales performance against monthly targets
SELECT
    o.sales_rep,
    COUNT(o.order_id) AS order_count,
    ROUND(SUM(o.total_sale), 2) AS actual_sales,
    t.monthly_target,
    ROUND(
        100.0 * SUM(o.total_sale) / t.monthly_target,
        2
    ) AS achievement_percentage
FROM orders o
INNER JOIN sales_targets t
    ON o.sales_rep = t.sales_rep
GROUP BY
    o.sales_rep,
    t.monthly_target
ORDER BY achievement_percentage DESC;


-- ============================================================
-- STEP 6: SUBQUERIES & CTE
-- ============================================================

-- Orders above average sale
SELECT
    order_id,
    order_date,
    customer,
    sales_rep,
    total_sale
FROM orders
WHERE total_sale > (
    SELECT AVG(total_sale)
    FROM orders
)
ORDER BY total_sale DESC;

-- Sales reps above average sales
SELECT
    sales_rep,
    ROUND(SUM(total_sale), 2) AS total_sales
FROM orders
GROUP BY sales_rep
HAVING SUM(total_sale) > (
    SELECT AVG(rep_sales)
    FROM (
        SELECT SUM(total_sale) AS rep_sales
        FROM orders
        GROUP BY sales_rep
    )
)
ORDER BY total_sales DESC;

-- CTE for sales representative performance
WITH rep_sales AS (
    SELECT
        sales_rep,
        ROUND(SUM(total_sale), 2) AS total_sales,
        COUNT(order_id) AS order_count
    FROM orders
    GROUP BY sales_rep
)
SELECT
    sales_rep,
    total_sales,
    order_count,
    ROUND(total_sales / order_count, 2) AS average_order_value
FROM rep_sales
ORDER BY total_sales DESC;


-- ============================================================
-- STEP 7: WINDOW FUNCTIONS
-- ============================================================

-- Rank sales representatives
SELECT
    sales_rep,
    ROUND(SUM(total_sale), 2) AS total_sales,
    RANK() OVER (
        ORDER BY SUM(total_sale) DESC
    ) AS sales_rank
FROM orders
GROUP BY sales_rep
ORDER BY sales_rank;

-- Rank orders within each sales representative
SELECT
    order_id,
    order_date,
    sales_rep,
    total_sale,
    ROW_NUMBER() OVER (
        PARTITION BY sales_rep
        ORDER BY total_sale DESC
    ) AS rep_order_rank
FROM orders
ORDER BY sales_rep, rep_order_rank;


-- ============================================================
-- STEP 8: BUSINESS ANALYSIS
-- ============================================================

-- Sales representative performance
SELECT
    sales_rep,
    COUNT(order_id) AS total_orders,
    SUM(
        CASE WHEN status = 'Completed'
        THEN 1 ELSE 0 END
    ) AS completed_orders,
    ROUND(SUM(total_sale), 2) AS total_sales,
    ROUND(
        SUM(
            CASE WHEN status = 'Completed'
            THEN total_sale ELSE 0 END
        ),
        2
    ) AS completed_sales,
    ROUND(
        100.0 *
        SUM(
            CASE WHEN status = 'Completed'
            THEN 1 ELSE 0 END
        ) / COUNT(order_id),
        2
    ) AS completion_rate
FROM orders
GROUP BY sales_rep
ORDER BY completion_rate DESC;

-- Category performance
SELECT
    category,
    COUNT(order_id) AS total_orders,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(total_sale), 2) AS total_sales,
    ROUND(AVG(total_sale), 2) AS average_sale
FROM orders
GROUP BY category
ORDER BY total_sales DESC;

-- Product performance
SELECT
    product,
    COUNT(order_id) AS total_orders,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(total_sale), 2) AS total_sales,
    ROUND(AVG(total_sale), 2) AS average_sale
FROM orders
GROUP BY product
ORDER BY total_sales DESC;

-- Region performance
SELECT
    region,
    COUNT(order_id) AS total_orders,
    COUNT(DISTINCT customer) AS unique_customers,
    ROUND(SUM(total_sale), 2) AS total_sales,
    ROUND(AVG(total_sale), 2) AS average_sale
FROM orders
GROUP BY region
ORDER BY total_sales DESC;

-- Customer performance
SELECT
    customer,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(total_sale), 2) AS total_sales,
    ROUND(AVG(total_sale), 2) AS average_sale
FROM orders
GROUP BY customer
ORDER BY total_sales DESC;


-- ============================================================
-- STEP 9: FINAL INTERVIEW QUERY
-- ============================================================

WITH rep_performance AS (
    SELECT
        o.sales_rep,
        COUNT(o.order_id) AS total_orders,
        ROUND(SUM(o.total_sale), 2) AS total_sales,
        t.monthly_target
    FROM orders o
    INNER JOIN sales_targets t
        ON o.sales_rep = t.sales_rep
    GROUP BY
        o.sales_rep,
        t.monthly_target
)
SELECT
    sales_rep,
    total_orders,
    total_sales,
    monthly_target,
    ROUND(
        100.0 * total_sales / monthly_target,
        2
    ) AS achievement_percentage,
    RANK() OVER (
        ORDER BY total_sales DESC
    ) AS sales_rank
FROM rep_performance
ORDER BY sales_rank;


-- ============================================================
-- END OF SQL ANALYSIS
-- ============================================================