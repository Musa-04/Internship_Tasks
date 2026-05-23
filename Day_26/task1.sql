SELECT MONTH(order_date) AS month,
SUM(total_amount) AS monthly_sales
FROM orders
GROUP BY MONTH(order_date);