-- -------------------------------------------------------
-- TASK 4 : Numerical Functions
-- Testing basic numeric functions used in analysis.
-- -------------------------------------------------------

CREATE TABLE orders (
order_id INT PRIMARY KEY,
price DECIMAL(10,3)
);

INSERT INTO orders VALUES
(1,25.678),
(2,19.234),
(3,10.978),
(4,-7.657);

-- rounding price to 2 decimal places
SELECT order_id, ROUND(price,2) AS rounded_price
FROM orders;

-- rounding price upward
SELECT order_id, CEILING(price) AS upper_price
FROM orders;

-- rounding price downward
SELECT order_id, FLOOR(price) AS lower_price
FROM orders;

-- converting negative values to positive
SELECT order_id, ABS(price) AS absolute_value
FROM orders;

-- power function example
SELECT POWER(5,2) AS power_result;

-- square root example
SELECT SQRT(64) AS square_root;

-- remainder example
SELECT MOD(10,3) AS remainder_value;