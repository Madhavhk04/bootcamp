USE amazon;

DELIMITER //
CREATE PROCEDURE select_all_products()
BEGIN
    SELECT * FROM items;
END //
DELIMITER ;

CALL select_all_products();

DROP PROCEDURE select_all_products;

DELIMITER $$
CREATE FUNCTION get_total_revenue()
RETURNS INT
DETERMINISTIC 
BEGIN
DECLARE total_revenue INT;
SELECT SUM(p.amount) INTO total_revenue
FROM payments p
INNER JOIN orders o ON p.order_id = o.order_id
WHERE p.payment_status = 'completed';
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
DELIMITER ;

CALL get_item_details(1);

DELIMITER //
CREATE PROCEDURE get_item_count(OUT item_count INT)
BEGIN
    SELECT COUNT(*) INTO item_count FROM items;
END //
DELIMITER ;

CALL get_item_count(@item_count);
SELECT @item_count AS item_count;

DELIMITER //
DECLARE @customer_count INT;

SELECT @customer_count = COUNT(*)
FROM customers;

PRINT 'Number of customers: ' + CAST(@customer_count AS VARCHAR(10));
DELIMITER ;

DELIMITER //
DECLARE @total_price INT;

SELECT @total_price = SUM(price)
FROM items
WHERE item_name = 'HP Laptop';
PRINT 'Total price of all HP Laptops: ' + CAST(@total_price AS VARCHAR(20));
DELIMITER ;
