-- -------------------------------------------------------
-- TASK 5 : E-Commerce Sales Analysis
-- Small project to analyze sales data similar to Amazon.
-- -------------------------------------------------------

CREATE DATABASE amazon_analysis;

USE amazon_analysis;

-- customers table
CREATE TABLE customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
city VARCHAR(50),
state VARCHAR(50),
signup_date DATE
);

INSERT INTO customers VALUES
(1,'Amit','Delhi','Delhi','2023-01-10'),
(2,'Rahul','Mumbai','Maharashtra','2023-02-11'),
(3,'Sneha','Bangalore','Karnataka','2023-03-12'),
(4,'Pooja','Hyderabad','Telangana','2023-04-15'),
(5,'Kiran','Chennai','Tamil Nadu','2023-05-10');

-- products table
CREATE TABLE products (
product_id INT PRIMARY KEY,
product_name VARCHAR(50),
category VARCHAR(50),
price INT
);

INSERT INTO products VALUES
(101,'Laptop','Electronics',60000),
(102,'Mobile','Electronics',30000),
(103,'Headphones','Electronics',2000),
(104,'Office Chair','Furniture',8000),
(105,'Coffee Maker','Home',3500);

-- orders table
CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
total_amount INT,
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders VALUES
(1001,1,'2024-01-05',62000),
(1002,2,'2024-01-10',30000),
(1003,3,'2024-02-12',2000),
(1004,1,'2024-03-10',8000),
(1005,4,'2024-03-20',3500),
(1006,5,'2024-04-11',30000);

-- order items table
CREATE TABLE orderitems (
order_item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT,
price INT,
FOREIGN KEY (order_id) REFERENCES orders(order_id),
FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO orderitems VALUES
(1,1001,101,1,60000),
(2,1001,103,1,2000),
(3,1002,102,1,30000),
(4,1003,103,1,2000),
(5,1004,104,1,8000),
(6,1005,105,1,3500),
(7,1006,102,1,30000);

-- total sales of the company
SELECT SUM(total_amount) AS total_sales
FROM orders;

-- sales by product category
SELECT category, SUM(price * quantity) AS category_sales
FROM orderitems
JOIN products ON orderitems.product_id = products.product_id
GROUP BY category;

-- number of orders per city
SELECT city, COUNT(order_id) AS total_orders
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY city;

-- average order value per customer
SELECT customer_id, AVG(total_amount) AS avg_order_value
FROM orders
GROUP BY customer_id;

-- highest spending customer
SELECT customers.customer_name, SUM(orders.total_amount) AS total_spent
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_name
ORDER BY total_spent DESC
LIMIT 1;

-- monthly sales report
SELECT MONTH(order_date) AS month,
YEAR(order_date) AS year,
SUM(total_amount) AS monthly_sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;