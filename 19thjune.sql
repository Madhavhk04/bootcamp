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
