CREATE TABLE employee (
emp_id INT PRIMARY KEY,
name VARCHAR(50),
age INT,
salary INT,
dept_id INT,
hire_date DATE,
manager_id INT
);

INSERT INTO employee VALUES
(1,'Arun',30,60000,201,'2018-05-10',101),
(2,'Rahul',28,45000,202,'2020-03-15',102),
(3,'Sneha',26,30000,203,'2021-06-20',101),
(4,'Kiran',35,75000,201,'2016-01-10',103),
(5,'Pooja',32,55000,204,'2017-07-11',101),
(6,'Ramesh',29,28000,205,'2022-02-14',104),
(7,'Divya',31,52000,202,'2019-04-09',102),
(8,'Ajay',27,35000,203,'2021-09-19',103),
(9,'Meena',33,48000,204,'2018-12-01',101),
(10,'Suresh',36,82000,201,'2015-06-21',103),
(11,'Anita',25,26000,205,'2023-01-15',104),
(12,'Vikram',34,67000,202,'2017-08-25',102),
(13,'Neha',29,39000,203,'2020-11-05',103),
(14,'Ravi',40,90000,201,'2014-03-18',103),
(15,'Lakshmi',30,47000,204,'2019-10-30',101);

CREATE TABLE departments (
dept_id INT PRIMARY KEY,
dept_name VARCHAR(50),
dept_count INT,
location VARCHAR(50)
);

INSERT INTO departments VALUES
(201,'IT',5,'Bangalore'),
(202,'HR',4,'Hyderabad'),
(203,'Finance',3,'Chennai'),
(204,'Sales',4,'Mumbai'),
(205,'Support',3,'Delhi');

CREATE TABLE customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO customers VALUES
(1,'Amit','Delhi'),
(2,'Rahul','Mumbai'),
(3,'Sneha','Bangalore'),
(4,'Pooja','Hyderabad'),
(5,'Kiran','Chennai');

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
amount INT,
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders VALUES
(101,1,'2024-01-10',2000),
(102,2,'2024-01-12',3500),
(103,3,'2024-02-05',1500),
(104,1,'2024-02-11',4500),
(105,4,'2024-03-01',2200);