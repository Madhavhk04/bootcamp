-- DQL STATEMENTS
-- 1) DQL stands for Data Query Language.

-- SELECT
-- Used to fetch rows selected from one or more tables.
-- SELECT can be utilized in several ways:
-- A) SELECT with DISTINCT Clause
-- The DISTINCT Clause after SELECT removes duplicate rows from the result set.
SELECT DISTINCT cname, addr FROM customer;

-- B) SELECT all columns(*)
SELECT * FROM orders;

-- C) SELECT by column name
SELECT oid FROM orders;

-- D) SELECT with LIKE(%)
-- Useful for searching using parts of the name
-- a) "dhav" appearing anywhere
SELECT * FROM customer WHERE cname LIKE "%dhav%";

-- b) Starts With "Mad"
SELECT * FROM customer WHERE cname LIKE "Mad%";

-- c) Ends With "hav"
SELECT * FROM customer WHERE cname LIKE "%hav";

-- E) SELECT with CASE or IF
-- a) CASE
SELECT cid,
	   cname,
       CASE WHEN cid > 105 THEN 'Active' ELSE 'Inactive' END AS 'Status'
FROM customer;

-- b) IF
SELECT cid,
	   cname,
       IF(cid > 105, 'Active', 'Inactive') AS 'Status'
FROM customer;

-- F) SELECT with a LIMIT Clause
SELECT * 
FROM customer
ORDER BY cid
LIMIT 3;

-- G) SELECT with WHERE
SELECT * FROM customer WHERE cname = "Madhav";

-- ------------------------------------------TASKS-------------------------------------------------------------
/*
1) Write a query to retrieve the unique categories of products from the products table.
2) Write a query to retrieve the customer ID, customer name, and the length of their address
   as address_length from the customer table.
3) Write a query to retrieve the order ID, customer name, product name, and the concatenated
   string 'Order for [product name] by [customer name]' as order_description from the orders, customer,
   and products tables.
4) Write a query to retrieve the product ID, product name, price, and a new column price_category that categorizes
   the products based on their price range (e.g., 'Low' for prices less than 10000, 'Medium' for prices between 10000
   and 50000, and 'High' for prices greater than 50000).
5) Write a query to retrieve the customer ID, customer name, and the total order amount for each customer.
   The total order amount should be retrieved from a subquery that calculates the sum of order amounts for each
   customer.
*/

-- --------------------------------------------QUERIES-----------------------------------------------------------
-- 1)
SELECT DISTINCT category 
FROM products;

-- 2)
SELECT cid, cname, LENGTH(addr) AS address_length
FROM customer;

-- 3)
SELECT o.oid, c.cname, p.pname, CONCAT('Order for ', p.pname, ' by ', c.cname) AS order_description
FROM orders o
JOIN customer c ON o.cid = c.cid
JOIN products p ON o.pid = p.pid;

-- 4)
SELECT pid, pname, price,
       CASE
           WHEN price < 10000 THEN 'Low'
           WHEN price BETWEEN 10000 AND 50000 THEN 'Medium'
           ELSE 'High'
       END AS price_category
FROM products;

-- 5)
SELECT c.cid, c.cname, (
    SELECT SUM(amt)
    FROM orders o
    WHERE o.cid = c.cid
) AS total_order_amount
FROM customer c;
