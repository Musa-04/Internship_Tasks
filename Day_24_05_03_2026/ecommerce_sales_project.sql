-- =====================================
-- ECOMMERCE SALES ANALYSIS PROJECT
-- =====================================

-- 1. CREATE DATABASE
CREATE DATABASE ecommerce_db;

-- 2. USE DATABASE
USE ecommerce_db;

-- =====================================
-- CUSTOMERS TABLE
-- =====================================

CREATE TABLE customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
city VARCHAR(50),
state VARCHAR(50),
signup_date DATE
);

-- INSERT DATA

INSERT INTO customers VALUES
(1,'Amit Sharma','Delhi','Delhi','2022-01-10'),
(2,'Rahul Verma','Mumbai','Maharashtra','2022-03-15'),
(3,'Sneha Reddy','Bangalore','Karnataka','2023-02-20'),
(4,'Pooja Singh','Hyderabad','Telangana','2023-05-11'),
(5,'Kiran Kumar','Chennai','Tamil Nadu','2024-01-18');

-- =====================================
-- PRODUCTS TABLE
-- =====================================

CREATE TABLE products (
product_id INT PRIMARY KEY,
product_name VARCHAR(50),
category VARCHAR(50),
price INT
);

INSERT INTO products VALUES
(101,'Laptop','Electronics',60000),
(102,'Mobile Phone','Electronics',30000),
(103,'Headphones','Electronics',2000),
(104,'Office Chair','Furniture',8000),
(105,'Coffee Maker','Home Appliances',3500);

-- =====================================
-- ORDERS TABLE
-- =====================================

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
total_amount INT,
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders VALUES
(1001,1,'2024-01-05',62000),
(1002,2,'2024-01-15',32000),
(1003,3,'2024-02-01',2000),
(1004,1,'2024-02-20',8000),
(1005,4,'2024-03-10',3500),
(1006,5,'2024-03-18',30000);

-- =====================================
-- ORDER ITEMS TABLE
-- =====================================

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
(4,1002,103,1,2000),
(5,1003,103,1,2000),
(6,1004,104,1,8000),
(7,1005,105,1,3500),
(8,1006,102,1,30000);

-- =====================================
-- ANALYTICAL QUERIES
-- =====================================

-- 1 TOTAL REVENUE

SELECT SUM(total_amount) AS total_revenue
FROM orders;


-- 2 TOTAL ORDERS

SELECT COUNT(*) AS total_orders
FROM orders;


-- 3 AVERAGE ORDER VALUE

SELECT AVG(total_amount) AS average_order_value
FROM orders;


-- 4 TOP 5 SELLING PRODUCTS

SELECT 
products.product_name,
SUM(orderitems.quantity) AS total_sold
FROM orderitems
JOIN products
ON orderitems.product_id = products.product_id
GROUP BY products.product_name
ORDER BY total_sold DESC
LIMIT 5;


-- 5 TOP CUSTOMERS

SELECT 
customers.customer_name,
SUM(orders.total_amount) AS total_spent
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_name
ORDER BY total_spent DESC
LIMIT 5;


-- 6 SALES BY CUSTOMER

SELECT 
customers.customer_name,
SUM(orders.total_amount) AS total_sales
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_name;


-- 7 SALES BY MONTH

SELECT 
MONTH(order_date) AS month,
SUM(total_amount) AS monthly_sales
FROM orders
GROUP BY MONTH(order_date);


-- 8 SALES BY REGION

SELECT 
customers.state,
SUM(orders.total_amount) AS total_sales
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
GROUP BY customers.state;