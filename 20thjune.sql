CREATE DATABASE ShopDB;
USE ShopDB;

-- Products - product_id, product_name, price, stock_quantity, city
CREATE TABLE products (
    product_id INT(3) PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock_quantity INT(5),
    city VARCHAR(30) CHECK(city IN ('Mumbai', 'Delhi'))
);

-- Customers - customer_id, customer_name, age, address
CREATE TABLE customers (
    customer_id INT(3) PRIMARY KEY,
    customer_name VARCHAR(30) NOT NULL,
    age INT(3),
    address VARCHAR(50)
);

-- Orders - order_id, customer_id, product_id, amount
CREATE TABLE orders (
    order_id INT(3) PRIMARY KEY,
    customer_id INT(3),
    product_id INT(3),
    amount INT(10) NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);

-- Payments - payment_id, order_id, amount, payment_mode, payment_status, timestamp
CREATE TABLE payments (
    payment_id INT(3) PRIMARY KEY,
    order_id INT(3),
    amount INT(10) NOT NULL,
    payment_mode VARCHAR(30) CHECK(payment_mode IN ('upi', 'credit', 'debit')),
    payment_status VARCHAR(30),
    timestamp TIMESTAMP,
    FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

-- Inserting values into products table
INSERT INTO products VALUES (1, 'HP Laptop', 50000, 15, 'Mumbai');
INSERT INTO products VALUES (2, 'Realme Mobile', 20000, 30, 'Delhi');
INSERT INTO products VALUES (3, 'Boat Earpods', 3000, 50, 'Delhi');
INSERT INTO products VALUES (4, 'Lenovo Laptop', 40000, 15, 'Mumbai');
INSERT INTO products VALUES (5, 'Charger', 1000, 0, 'Mumbai');
INSERT INTO products VALUES (6, 'MacBook', 78000, 6, 'Delhi');
INSERT INTO products VALUES (7, 'JBL Speaker', 6000, 2, 'Delhi');
INSERT INTO products VALUES (8, 'Asus Laptop', 50000, 15, 'Delhi');

-- Inserting values into customers table
INSERT INTO customers VALUES (101, 'Ravi Kumar', 30, 'Mumbai, India');
INSERT INTO customers VALUES (102, 'Rahul Sharma', 25, 'Delhi, India');
INSERT INTO customers VALUES (103, 'Simran Kaur', 32, 'Delhi, India');
INSERT INTO customers VALUES (104, 'Purvesh Mehta', 28, 'Mumbai, India');
INSERT INTO customers VALUES (105, 'Sanjana Singh', 22, 'Mumbai, India');

-- Inserting values into orders table
INSERT INTO orders VALUES (10001, 102, 3, 2700);
INSERT INTO orders VALUES (10002, 104, 2, 18000);
INSERT INTO orders VALUES (10003, 105, 5, 900);
INSERT INTO orders VALUES (10004, 101, 1, 46000);

-- Inserting values into payments table
INSERT INTO payments VALUES (1, 10001, 2700, 'upi', 'completed', '2024-05-01 08:00:00');
INSERT INTO payments VALUES (2, 10002, 18000, 'credit', 'completed', '2024-05-01 08:10:00');
INSERT INTO payments VALUES (3, 10003, 900, 'debit', 'in process', '2024-05-01 08:15:00');

-- SUBQUERIES

-- SINGLE ROW SUBQUERIES

-- Example 1: Find the customer who placed the order with the highest amount
SELECT customer_name 
FROM customers 
WHERE customer_id = (SELECT customer_id FROM orders ORDER BY amount DESC LIMIT 1);

-- Example 2: Find the product with the highest price
SELECT product_name 
FROM products 
WHERE price = (SELECT MAX(price) FROM products);

-- MULTIPLE-ROW SUBQUERIES

-- Example 1: Find all customers who have placed an order
SELECT customer_name 
FROM customers 
WHERE customer_id IN (SELECT customer_id FROM orders);

-- Example 2: Find all customers who have placed an order for a product from Mumbai
SELECT customer_name 
FROM customers 
WHERE customer_id IN (
    SELECT customer_id FROM orders 
    WHERE product_id IN (SELECT product_id FROM products WHERE city = 'Mumbai')
);

-- CORRELATED SUBQUERIES

-- Example 1: Products with Price Higher than Location Average
SELECT product_name, price 
FROM products p 
WHERE price > (
    SELECT AVG(price) 
    FROM products 
    WHERE city = p.city
);

-- Example 2: Customers with Orders Exceeding Average Order Amount
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

-- JOINS

-- INNER JOIN with subquery
-- Example: Retrieve the products with their corresponding orders where the product price is greater than 1000
SELECT p.product_name, o.order_id, o.amount 
FROM products p 
INNER JOIN (SELECT * FROM orders) o ON p.product_id = o.product_id 
WHERE p.price > 1000;

-- LEFT JOIN with aggregate functions
-- Example: Retrieve all products and their total orders' amounts, even if there are no orders
SELECT p.product_name, SUM(o.amount) AS total_orders_amount 
FROM products p 
LEFT JOIN orders o ON p.product_id = o.product_id 
GROUP BY p.product_name;

-- RIGHT JOIN with date and time functions
-- Example: Retrieve all orders and their corresponding payment status and timestamp, even if there is no payment record
SELECT o.order_id, o.amount, p.payment_status, p.timestamp 
FROM orders o 
RIGHT JOIN payments p ON o.order_id = p.order_id;

-- Analytics functions / Advanced functions

-- RANK
-- Example: Display rank of products on the basis of price using RANK() FUNCTION
SELECT product_id, product_name, price, RANK() OVER (ORDER BY price DESC) AS price_rank 
FROM products;

-- DENSE_RANK
-- Example: Display rank of products on the basis of price using DENSE_RANK() FUNCTION
SELECT product_id, product_name, price, DENSE_RANK() OVER (ORDER BY price DESC) AS price_rank 
FROM products;

-- ROW_NUMBER
-- Example: Find Unique Row number of the Customer table using Row number Function
SELECT ROW_NUMBER() OVER (ORDER BY age DESC) AS row_num, customer_id, customer_name, age, address 
FROM customers;

-- CUME_DIST
-- Example: Find Cumulative Distribution of payment done based on amount spent
SELECT order_id, amount, CUME_DIST() OVER (ORDER BY amount) AS cumulative_distribution 
FROM payments;

-- LAG
-- Example: Find the previous price of products within the same city using LAG() FUNCTION
SELECT product_name, price, city, LAG(price) OVER (PARTITION BY city ORDER BY price) AS previous_price 
FROM products;

-- LEAD
-- Example: Find the next price of products within the same city using LEAD() FUNCTION
SELECT product_name, price, city, LEAD(price) OVER (PARTITION BY city ORDER BY price) AS next_price 
FROM products;
