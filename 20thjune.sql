CREATE DATABASE ShopDB;
USE ShopDB;

CREATE TABLE products (
    product_id INT(3) PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock_quantity INT(5),
    city VARCHAR(30) CHECK(city IN ('Mumbai', 'Delhi'))
);

CREATE TABLE customers (
    customer_id INT(3) PRIMARY KEY,
    customer_name VARCHAR(30) NOT NULL,
    age INT(3),
    address VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT(3) PRIMARY KEY,
    customer_id INT(3),
    product_id INT(3),
    amount INT(10) NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);

CREATE TABLE payments (
    payment_id INT(3) PRIMARY KEY,
    order_id INT(3),
    amount INT(10) NOT NULL,
    payment_mode VARCHAR(30) CHECK(payment_mode IN ('upi', 'credit', 'debit')),
    payment_status VARCHAR(30),
    timestamp TIMESTAMP,
    FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

INSERT INTO products VALUES (1, 'HP Laptop', 50000, 15, 'Mumbai');
INSERT INTO products VALUES (2, 'Realme Mobile', 20000, 30, 'Delhi');
INSERT INTO products VALUES (3, 'Boat Earpods', 3000, 50, 'Delhi');
INSERT INTO products VALUES (4, 'Lenovo Laptop', 40000, 15, 'Mumbai');
INSERT INTO products VALUES (5, 'Charger', 1000, 0, 'Mumbai');
INSERT INTO products VALUES (6, 'MacBook', 78000, 6, 'Delhi');
INSERT INTO products VALUES (7, 'JBL Speaker', 6000, 2, 'Delhi');
INSERT INTO products VALUES (8, 'Asus Laptop', 50000, 15, 'Delhi');

INSERT INTO customers VALUES (101, 'Madhav', 30, 'Mumbai, India');
INSERT INTO customers VALUES (102, 'Arpita', 25, 'Delhi, India');
INSERT INTO customers VALUES (103, 'Adwaid', 32, 'Delhi, India');
INSERT INTO customers VALUES (104, 'Shahul', 28, 'Mumbai, India');
INSERT INTO customers VALUES (105, 'Aadhil', 22, 'Mumbai, India');

INSERT INTO orders VALUES (10001, 102, 3, 2700);
INSERT INTO orders VALUES (10002, 104, 2, 18000);
INSERT INTO orders VALUES (10003, 105, 5, 900);
INSERT INTO orders VALUES (10004, 101, 1, 46000);

INSERT INTO payments VALUES (1, 10001, 2700, 'upi', 'completed', '2024-05-01 08:00:00');
INSERT INTO payments VALUES (2, 10002, 18000, 'credit', 'completed', '2024-05-01 08:10:00');
INSERT INTO payments VALUES (3, 10003, 900, 'debit', 'in process', '2024-05-01 08:15:00');

SELECT customer_name 
FROM customers 
WHERE customer_id = (SELECT customer_id FROM orders ORDER BY amount DESC LIMIT 1);

SELECT product_name 
FROM products 
WHERE price = (SELECT MAX(price) FROM products);

SELECT customer_name 
FROM customers 
WHERE customer_id IN (SELECT customer_id FROM orders);

SELECT customer_name 
FROM customers 
WHERE customer_id IN (
    SELECT customer_id FROM orders 
    WHERE product_id IN (SELECT product_id FROM products WHERE city = 'Mumbai')
);

SELECT product_name, price 
FROM products p 
WHERE price > (
    SELECT AVG(price) 
    FROM products 
    WHERE city = p.city
);

SELECT customer_name 
FROM customers c 
WHERE EXISTS (
    SELECT 1 
    FROM orders o 
    WHERE o.customer_id = c.customer_id 
    GROUP BY o.customer_id 
    HAVING AVG(o.amount) > (
        SELECT AVG(amount) 
        FROM orders
    )
);

SELECT p.product_name, o.order_id, o.amount 
FROM products p 
INNER JOIN (SELECT * FROM orders) o ON p.product_id = o.product_id 
WHERE p.price > 1000;

SELECT p.product_name, SUM(o.amount) AS total_orders_amount 
FROM products p 
LEFT JOIN orders o ON p.product_id = o.product_id 
GROUP BY p.product_name;

SELECT o.order_id, o.amount, p.payment_status, p.timestamp 
FROM orders o 
RIGHT JOIN payments p ON o.order_id = p.order_id;

SELECT product_id, product_name, price, RANK() OVER (ORDER BY price DESC) AS price_rank 
FROM products;

SELECT product_id, product_name, price, DENSE_RANK() OVER (ORDER BY price DESC) AS price_rank 
FROM products;

SELECT ROW_NUMBER() OVER (ORDER BY age DESC) AS row_num, customer_id, customer_name, age, address 
FROM customers;

SELECT order_id, amount, CUME_DIST() OVER (ORDER BY amount) AS cumulative_distribution 
FROM payments;

SELECT product_name, price, city, LAG(price) OVER (PARTITION BY city ORDER BY price) AS lag_price 
FROM products;

SELECT product_name, price, city, LEAD(price) OVER (PARTITION BY city ORDER BY price) AS lead_price 
FROM products;
