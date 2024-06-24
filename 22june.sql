
SELECT DISTINCT cname, addr FROM customer;

-- B) SELECT all columns(*)
SELECT * FROM orders;

-- C) SELECT by column name
SELECT oid FROM orders;


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
