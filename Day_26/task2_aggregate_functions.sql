-- -------------------------------------------------------
-- TASK 2 : Aggregate Functions
-- Here we create a sales table and apply functions
-- like SUM, COUNT, AVG, MIN and MAX.
-- -------------------------------------------------------

CREATE TABLE sales (
id INT PRIMARY KEY,
product_name VARCHAR(50),
price DECIMAL(10,2)
);

-- inserting sample sales data
INSERT INTO sales VALUES
(1,'Laptop',65000),
(2,'Mobile',30000),
(3,'Headphones',2000),
(4,'Keyboard',1500),
(5,'Mouse',800),
(6,'Monitor',12000),
(7,'Printer',9000),
(8,'Tablet',25000),
(9,'Speaker',3500),
(10,'Camera',45000),
(11,'Smartwatch',7000),
(12,'Router',2500),
(13,'SSD',6000),
(14,'Hard Disk',5500),
(15,'Charger',900),
(16,'Projector',40000),
(17,'Graphics Card',50000),
(18,'RAM',3500),
(19,'Microphone',2800),
(20,'Gaming Console',48000);

-- total number of products
SELECT COUNT(*) AS total_products FROM sales;

-- total sales amount
SELECT SUM(price) AS total_sales FROM sales;

-- lowest price product
SELECT MIN(price) AS minimum_price FROM sales;

-- highest price product
SELECT MAX(price) AS maximum_price FROM sales;

-- average price
SELECT AVG(price) AS average_price FROM sales;