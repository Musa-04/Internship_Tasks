-- -------------------------------------------------------
-- TASK 3 : GROUP BY and HAVING
-- This example calculates average salary per department
-- and filters departments based on total salary.
-- -------------------------------------------------------

CREATE TABLE departments (
dept_name VARCHAR(20),
salary INT
);

-- inserting department salary data
INSERT INTO departments VALUES
('IT',40000),
('IT',55000),
('HR',35000),
('Finance',43000),
('HR',45000),
('IT',60000),
('Finance',50000),
('HR',30000);

-- average salary in each department
SELECT dept_name, AVG(salary)
FROM departments
GROUP BY dept_name;

-- departments where total salary is greater than 100000
SELECT dept_name, SUM(salary)
FROM departments
GROUP BY dept_name
HAVING SUM(salary) > 100000;