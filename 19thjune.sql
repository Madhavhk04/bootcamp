CREATE DATABASE amazon;

USE amazon;

CREATE TABLE products (
    pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(5),
    location VARCHAR(30) CHECK(location IN ('Bangalore', 'Hyderabad'))
);

CREATE TABLE customer (
    cid INT(3) PRIMARY KEY,
    cname VARCHAR(30) NOT NULL,
    age INT(3),
    addr VARCHAR(50)
);

CREATE TABLE orders (
    oid INT(3) PRIMARY KEY,
    cid INT(3),
    pid INT(3),
    amt INT(10) NOT NULL,
    FOREIGN KEY(cid) REFERENCES customer(cid),
    FOREIGN KEY(pid) REFERENCES products(pid)
);

CREATE TABLE payment (
    pay_id INT(3) PRIMARY KEY,
    oid INT(3),
    amount INT(10) NOT NULL,
    mode VARCHAR(30) CHECK(mode IN('upi', 'credit', 'debit')),
    status VARCHAR(30),
    FOREIGN KEY(oid) REFERENCES orders(oid)
);

CREATE TABLE employee (
    eid INT(4) PRIMARY KEY,
    ename VARCHAR(40) NOT NULL,
    phone_no INT(10) NOT NULL,
    department VARCHAR(40) NOT NULL,
    manager_id INT(4)
);

INSERT INTO products VALUES
(1, 'Dell Laptop', 50000, 15, 'Bangalore'),
(2, 'Realme Mobile', 20000, 30, 'Hyderabad'),
(3, 'Boat Earpods', 3000, 50, 'Hyderabad'),
(4, 'Lenovo Laptop', 40000, 15, 'Bangalore'),
(5, 'Headset', 1000, 0, 'Bangalore'),
(6, 'MacBook', 78000, 6, 'Hyderabad'),
(7, 'JBL Speaker', 6000, 2, 'Hyderabad');

INSERT INTO customer VALUES
(101, 'Madhav', 30, 'fdslfjl'),
(102, 'Arpita', 25, 'fdslfjl'),
(103, 'Anjana', 32, 'fdslfjl'),
(104, 'Harsha', 28, 'fdslfjl'),
(105, 'Shahul', 22, 'fdslfjl');

INSERT INTO orders VALUES
(10001, 102, 3, 2700),
(10002, 104, 2, 18000),
(10003, 105, 5, 900),
(10004, 101, 1, 46000);

INSERT INTO payment VALUES
(1, 10001, 2700, 'upi', 'completed'),
(2, 10002, 18000, 'credit', 'completed'),
(3, 10003, 900, 'debit', 'in process');

INSERT INTO employee VALUES
(401, 'Rohan', 364832549, 'Analysis', 404),
(402, 'Rahul', 782654123, 'Delivery', 406),
(403, 'Shyam', 856471235, 'Delivery', 402),
(404, 'Neha', 724863287, 'Sales', 402),
(405, 'Sanjana', 125478954, 'HR', 404),
(406, 'Sanjay', 956478535, 'Tech', NULL);

SELECT * FROM products;

SELECT * FROM customer;

SELECT * FROM orders;

SELECT * FROM payment;

SELECT * FROM employee;

SELECT customer.cid, cname, orders.oid FROM orders 
INNER JOIN customer ON orders.cid = customer.cid;

SELECT customer.cid, cname, products.pid, pname, oid FROM orders
INNER JOIN products ON orders.pid = products.pid
INNER JOIN customer ON orders.cid = customer.cid;

SELECT products.pid, pname, amt, orders.oid FROM products
LEFT JOIN orders ON orders.pid = products.pid;

SELECT * FROM payment 
RIGHT JOIN orders ON orders.oid = payment.oid;

SELECT orders.oid, products.pid, pname, amt, price, stock, location FROM orders
LEFT JOIN products ON orders.pid = products.pid
UNION
SELECT orders.oid, products.pid, pname, amt, price, stock, location FROM orders
RIGHT JOIN products ON orders.pid = products.pid;

SELECT e1.ename AS Employee, e2.ename AS Manager FROM employee e1
INNER JOIN employee e2 ON e1.manager_id = e2.eid;

SELECT customer.cid, cname, orders.oid, amt FROM customer
CROSS JOIN orders ON customer.cid = orders.cid
WHERE amt > 3000;


-- Creating database
CREATE DATABASE amazon;

-- Using database
USE amazon;

-- Creating table Products - pid, pname, price, stock, location (Mumbai or Delhi)
CREATE TABLE products
(
    pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(5),
    location VARCHAR(30) CHECK(location IN ('Mumbai','Delhi'))
);

-- Creating table Customer - cid, cname, age, addr
CREATE TABLE customer
(
    cid INT(3) PRIMARY KEY,
    cname VARCHAR(30) NOT NULL,
    age INT(3),
    addr VARCHAR(50)
);

-- Creating table Orders - oid, cid, pid, amt
CREATE TABLE orders
(
    oid INT(3) PRIMARY KEY,
    cid INT(3),
    pid INT(3),
    amt INT(10) NOT NULL,
    FOREIGN KEY(cid) REFERENCES customer(cid),
    FOREIGN KEY(pid) REFERENCES products(pid)
);

-- Creating table Payment - pay_id, oid, amount, mode(upi, credit, debit), status
CREATE TABLE payment
(
    pay_id INT(3) PRIMARY KEY,
    oid INT(3),
    amount INT(10) NOT NULL,
    mode VARCHAR(30) CHECK(mode IN('upi','credit','debit')),
    status VARCHAR(30),
    FOREIGN KEY(oid) REFERENCES orders(oid)
);

-- Creating table Employee - eid, ename, phone_no, department, manager_id
CREATE TABLE employee(
    eid INT(4) PRIMARY KEY,
    ename VARCHAR(40) NOT NULL,
    phone_no INT(10) NOT NULL,
    department VARCHAR(40) NOT NULL,
    manager_id INT(4)
);

-- Anomalies

-- Update Anomaly
-- Imagine a situation where the price of the "HP Laptop" (ProductID: 1) needs to be updated from ₹50,000 to ₹52,000. Here's the potential update anomaly:
UPDATE products
SET price = 52000
WHERE pid = 1;

-- The problem arises because the actual selling price of a product might be stored in the Orders table. 
-- If you have existing orders for the "HP Laptop" placed at the old price (₹50,000), these orders won't be automatically updated to reflect the new price (₹52,000). 
-- This inconsistency can lead to issues like incorrect revenue calculations or customer disputes.

-- Delete Anomaly
-- Imagine a situation where a specific product, the "Charger" (ProductID: 5), becomes discontinued and needs to be removed from the database. Here's how a delete anomaly could occur:
-- You delete the "Charger" record from the Products table:
DELETE FROM products
WHERE pid = 5;

-- The problem arises if there are existing orders for the "Charger" in the Orders table. Deleting the product from Products would leave those orders referencing a non-existent product.

-- Insertion Anomaly
-- Imagine you want to create a new order for a customer (CustomerID: 106) who hasn't been added to the Customers table yet. Here's how an insertion anomaly could occur:
INSERT INTO orders (oid, cid, pid, amt)
VALUES (10005, 106, 2, 1);  -- Assuming ProductID 2 is 'Realme Mobile'

-- The insertion fails because the CustomerID (106) doesn't exist in the Customers table.

-- Candidate Keys
-- Candidate keys are attributes or combinations of attributes within a relation (table) that uniquely identify each tuple (row).
-- They are essential for maintaining data integrity and enforcing constraints within a database schema
-- Examples: pid, cid, oid, and pay_id are candidate keys in their respective tables ensuring the uniqueness of each product, customer, order, and payment.

-- Primary Key
-- It is a column or a set of columns that uniquely identifies each record in a table.
-- Example: pid in the products table
CREATE TABLE products
(
    pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(5),
    location VARCHAR(30) CHECK(location IN ('Mumbai','Delhi'))
);

-- Adding Primary Key to an already existing table
ALTER TABLE products
ADD PRIMARY KEY (pid);

-- Deleting Primary Key from a table
ALTER TABLE products
DROP PRIMARY KEY;

-- Foreign Key
-- It is a column or group of columns in a database that connects the data in one table to the data in another table.
-- Example: Establishing a connection between the Product table, Customer table and Orders table
CREATE TABLE orders
(
    oid INT(3) PRIMARY KEY,
    cid INT(3),
    pid INT(3),
    amt INT(10) NOT NULL,
    FOREIGN KEY(cid) REFERENCES customer(cid),
    FOREIGN KEY(pid) REFERENCES products(pid)
);

-- Adding Foreign key to an already existing table
ALTER TABLE orders 
ADD FOREIGN KEY(pid) REFERENCES products(pid);

-- Removing Foreign Key from a table
ALTER TABLE orders DROP FOREIGN KEY orders_ibfk_2;

-- Normalization
-- The process of minimizing redundancy from a relation or set of relations. Ensures a table structure that minimizes redundancy and improves data integrity.
-- First Normal Form (1NF)
-- Ensures a table structure that minimizes redundancy and improves data integrity.
-- Example of a table following 1NF
CREATE TABLE products
(
    pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(5),
    location VARCHAR(30) CHECK(location IN ('Mumbai','Delhi'))
);

-- Second Normal Form (2NF)
-- Table must be in 1NF.
-- All non-key attributes must depend on the entire primary key.
-- Example: Separate Order_Items table for additional product information
CREATE TABLE orders
(
    oid INT(3) PRIMARY KEY,
    cid INT(3),
    pid INT(3),
    amt INT(10) NOT NULL,
    FOREIGN KEY(cid) REFERENCES customer(cid),
    FOREIGN KEY(pid) REFERENCES products(pid)
);

CREATE TABLE order_items
(
    order_item_id INT(3) PRIMARY KEY,
    oid INT(3),
    pid INT(3),
    product_color VARCHAR(30),
    FOREIGN KEY(oid) REFERENCES orders(oid),
    FOREIGN KEY(pid) REFERENCES products(pid)
);

-- Third Normal Form (3NF)
-- Table must be in 2NF.
-- No transitive dependencies should exist.
-- Every non-key attribute must depend on the primary key, and only the primary key.
-- Example: Separate Customer_City table for city information
CREATE TABLE customer_city
(
    cid INT(3) PRIMARY KEY,
    city VARCHAR(30),
    FOREIGN KEY(cid) REFERENCES customer(cid)
);

-- Boyce-Codd Normal Form (BCNF)
-- A higher level of normalization than 3NF.
-- Ensures no non-trivial functional dependencies exist between attributes that are not part of some candidate key.
-- Example: Decompose Orders table to order_info and order_details
CREATE TABLE order_info
(
    oid INT(3) PRIMARY KEY,
    amt INT(10) NOT NULL,
    FOREIGN KEY(oid) REFERENCES orders(oid)
);

CREATE TABLE order_details
(
    oid INT(3),
    cid INT(3),
    pid INT(3),
    PRIMARY KEY(oid, cid, pid),
    FOREIGN KEY(oid) REFERENCES orders(oid),
    FOREIGN KEY(cid) REFERENCES customer(cid),
    FOREIGN KEY(pid) REFERENCES products(pid)
);

-- Questions and Answers

-- 1. What are potential data anomalies that could occur if the database is not normalized (specifically 1NF, 2NF, or 3NF)?
-- Answer: Data anomalies are inconsistencies or redundancies that can arise in a non-normalized database. These anomalies can lead to data integrity issues, making it difficult to insert, update, or delete data accurately.
-- Insertion Anomaly: Difficulty inserting complete data due to missing dependencies.
-- Deletion Anomaly: Deleting data from one table can unintentionally affect data in another table.
-- Update Anomaly: Updating data in one table might require repetitive changes in other tables to maintain consistency.

-- 2. Candidate Keys and Primary Key:
-- Query: Write a query to display the product information and choose the most appropriate attribute(s) as the primary key for the Products table. Justify your choice.
SELECT pid, pname, price, stock, location
FROM products;

-- 3. Foreign Keys:
-- Query: Write a query that joins the Orders and Customer tables using the foreign key relationship. This query should retrieve order details (order ID, customer name, product ID) for a specific customer (e.g., customer ID 102).
SELECT o.oid, c.cname, o.pid
FROM orders o
INNER JOIN customer c ON o.cid = c.cid
WHERE o.cid = 102;

-- 4. Normalization Levels (1NF, 2NF, 3NF):
-- Question: Describe the key differences between 1NF, 2NF, and 3NF.
-- Answer: 
-- 1NF - First Normal Form
-- Ensures single-valued attributes, no repeating groups, and unique rows.

-- 2NF - Second Normal Form
-- Ensures the table is in 1NF and all non-key attributes are fully dependent on the primary key, eliminating partial dependencies.

-- 3NF - Third Normal Form
-- Ensures the table is in 2NF and eliminates transitive dependencies, where non-key attributes depend only on the primary key.

-- 5. Boyce-Codd Normal Form (BCNF):
-- Question: How does BCNF differ from 3NF? When is it typically used?
-- Answer: 
-- BCNF (Boyce-Codd Normal Form) is a higher level of normalization compared
