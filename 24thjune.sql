



CREATE DATABASE amazon;
USE amazon;

CREATE TABLE items (
    item_id INT(3) PRIMARY KEY,
    item_name VARCHAR(50) NOT NULL,
    cost INT(10) NOT NULL,
    quantity INT(5),
    location VARCHAR(30) CHECK(location IN ('Mumbai', 'Delhi'))
);

CREATE TABLE clients (
    client_id INT(3) PRIMARY KEY,
    client_name VARCHAR(30) NOT NULL,
    age INT(3),
    residence VARCHAR(50)
);

CREATE TABLE purchases (
    purchase_id INT(3) PRIMARY KEY,
    client_id INT(3),
    item_id INT(3),
    total_cost INT(10) NOT NULL,
    FOREIGN KEY(client_id) REFERENCES clients(client_id),
    FOREIGN KEY(item_id) REFERENCES items(item_id)
);

CREATE TABLE transactions (
    transaction_id INT(3) PRIMARY KEY,
    purchase_id INT(3),
    amount INT(10) NOT NULL,
    payment_type VARCHAR(30) CHECK(payment_type IN ('upi', 'credit', 'debit')),
    payment_status VARCHAR(30),
    timestamp TIMESTAMP,
    FOREIGN KEY(purchase_id) REFERENCES purchases(purchase_id)
);

INSERT INTO items VALUES (1, 'Dell Laptop', 60000, 10, 'Mumbai');
INSERT INTO items VALUES (2, 'Samsung Mobile', 25000, 20, 'Delhi');
INSERT INTO items VALUES (3, 'Sony Headphones', 5000, 40, 'Delhi');
INSERT INTO items VALUES (4, 'Acer Laptop', 35000, 10, 'Mumbai');
INSERT INTO items VALUES (5, 'Wireless Charger', 2000, 0, 'Mumbai');
INSERT INTO items VALUES (6, 'iPad', 85000, 5, 'Delhi');
INSERT INTO items VALUES (7, 'Google Home', 8000, 3, 'Delhi');
INSERT INTO items VALUES (8, 'HP Laptop', 55000, 12, 'Delhi');

INSERT INTO clients VALUES (101, 'Rohan', 30, 'Mumbai, India');
INSERT INTO clients VALUES (102, 'Priya', 25, 'Delhi, India');
INSERT INTO clients VALUES (103, 'Karan', 32, 'Delhi, India');
INSERT INTO clients VALUES (104, 'Amit', 28, 'Mumbai, India');
INSERT INTO clients VALUES (105, 'Sita', 22, 'Mumbai, India');

INSERT INTO purchases VALUES (10001, 102, 3, 4500);
INSERT INTO purchases VALUES (10002, 104, 2, 23000);
INSERT INTO purchases VALUES (10003, 105, 5, 1800);
INSERT INTO purchases VALUES (10004, 101, 1, 54000);

INSERT INTO transactions VALUES (1, 10001, 4500, 'upi', 'completed', '2024-05-01 08:00:00');
INSERT INTO transactions VALUES (2, 10002, 23000, 'credit', 'completed', '2024-05-01 08:10:00');
INSERT INTO transactions VALUES (3, 10003, 1800, 'debit', 'in process', '2024-05-01 08:15:00');

SELECT client_name 
FROM clients 
WHERE client_id = (SELECT client_id FROM purchases ORDER BY total_cost DESC LIMIT 1);

SELECT item_name 
FROM items 
WHERE cost = (SELECT MAX(cost) FROM items);

SELECT client_name 
FROM clients 
WHERE client_id IN (SELECT client_id FROM purchases);

SELECT client_name 
FROM clients 
WHERE client_id IN (
    SELECT client_id FROM purchases 
    WHERE item_id IN (SELECT item_id FROM items WHERE location = 'Mumbai')
);

SELECT item_name, cost 
FROM items i 
WHERE cost > (
    SELECT AVG(cost) 
    FROM items 
    WHERE location = i.location
);

SELECT client_name 
FROM clients c 
WHERE EXISTS (
    SELECT 1 
    FROM purchases p 
    WHERE p.client_id = c.client_id 
    GROUP BY p.client_id 
    HAVING AVG(p.total_cost) > (
        SELECT AVG(total_cost) 
        FROM purchases
    )
);

SELECT i.item_name, p.purchase_id, p.total_cost 
FROM items i 
INNER JOIN (SELECT * FROM purchases) p ON i.item_id = p.item_id 
WHERE i.cost > 1000;

SELECT i.item_name, SUM(p.total_cost) AS total_purchases_cost 
FROM items i 
LEFT JOIN purchases p ON i.item_id = p.item_id 
GROUP BY i.item_name;

SELECT p.purchase_id, p.total_cost, t.payment_status, t.timestamp 
FROM purchases p 
RIGHT JOIN transactions t ON p.purchase_id = t.purchase_id;

SELECT item_id, item_name, cost, RANK() OVER (ORDER BY cost DESC) AS cost_rank 
FROM items;

SELECT item_id, item_name, cost, DENSE_RANK() OVER (ORDER BY cost DESC) AS cost_rank 
FROM items;

SELECT ROW_NUMBER() OVER (ORDER BY age DESC) AS row_num, client_id, client_name, age, residence 
FROM clients;

SELECT purchase_id, total_cost, CUME_DIST() OVER (ORDER BY total_cost) AS cumulative_distribution 
FROM transactions;

SELECT item_name, cost, location, LAG(cost) OVER (PARTITION BY location ORDER BY cost) AS lag_cost 
FROM items;

SELECT item_name, cost, location, LEAD(cost) OVER (PARTITION BY location ORDER BY cost) AS lead_cost 
FROM items;

DELIMITER //
CREATE PROCEDURE select_all_items()
BEGIN
    SELECT * FROM items;
END //
DELIMITER ;

CALL select_all_items();
DROP PROCEDURE select_all_items;

DELIMITER $$
CREATE FUNCTION get_total_revenue()
RETURNS INT
DETERMINISTIC 
BEGIN
DECLARE total_revenue INT; 
SELECT SUM(t.amount) INTO total_revenue
FROM transactions t
INNER JOIN purchases p ON t.purchase_id = p.purchase_id
WHERE t.payment_status = 'completed';
RETURN total_revenue; 
END$$
DELIMITER ;

SELECT get_total_revenue();
DROP FUNCTION IF EXISTS get_total_revenue;

DELIMITER //
CREATE PROCEDURE get_item_details(IN item_id INT)
BEGIN
    SELECT * FROM items WHERE item_id = item_id;
END //

CALL get_item_details(1);

DELIMITER //
CREATE PROCEDURE get_item_count(OUT item_count INT)
BEGIN
    SELECT COUNT(*) INTO item_count FROM items;
END //

CALL get_item_count(@item_count);
SELECT @item_count as item_count;
```