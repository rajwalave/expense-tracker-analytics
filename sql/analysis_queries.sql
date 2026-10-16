USE expense_analytics;

-- 1. Monthly spending trend
SELECT DATE_FORMAT(transaction_date, '%Y-%m') AS month,
       ROUND(SUM(amount_inr), 2) AS total_spend
FROM transactions
GROUP BY DATE_FORMAT(transaction_date, '%Y-%m')
ORDER BY month;

-- 2. Spend by category
SELECT category, ROUND(SUM(amount_inr), 2) AS total_spend,
       COUNT(*) AS transaction_count,
       ROUND(AVG(amount_inr), 2) AS average_transaction
FROM transactions
GROUP BY category
ORDER BY total_spend DESC;

-- 3. Payment method mix
SELECT payment_method, COUNT(*) AS transactions,
       ROUND(SUM(amount_inr), 2) AS total_spend
FROM transactions
GROUP BY payment_method
ORDER BY total_spend DESC;

-- 4. Weekday vs weekend
SELECT CASE WHEN DAYOFWEEK(transaction_date) IN (1,7)
            THEN 'Weekend' ELSE 'Weekday' END AS day_type,
       COUNT(*) AS transaction_count,
       ROUND(AVG(amount_inr), 2) AS average_amount,
       ROUND(SUM(amount_inr), 2) AS total_spend
FROM transactions
GROUP BY day_type;

-- 5. Largest transactions
SELECT transaction_date, category, merchant, amount_inr
FROM transactions
ORDER BY amount_inr DESC
LIMIT 10;

-- 6. Month-over-month change
WITH monthly AS (
    SELECT DATE_FORMAT(transaction_date, '%Y-%m') AS month,
           SUM(amount_inr) AS spend
    FROM transactions
    GROUP BY DATE_FORMAT(transaction_date, '%Y-%m')
)
SELECT month, ROUND(spend,2) AS spend,
       ROUND(spend - LAG(spend) OVER (ORDER BY month),2) AS change_inr,
       ROUND(100 * (spend / NULLIF(LAG(spend) OVER (ORDER BY month),0) - 1),2) AS change_pct
FROM monthly
ORDER BY month;
