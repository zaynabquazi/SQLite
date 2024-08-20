-- Select all columns from a table 
SELECT * FROM inventory;

-- Select few colomns from a table 

SELECT product_name, quantity FROM inventory; 

-- Select order by item lowest to highest 

SELECT * FROM inventory 
order by inventory_id ASC

-- Select order by item highest to lowest

SELECT * FROM inventory 
order by inventory_id DESC;

-- highest record from a table 

SELECT * FROM inventory 
order by inventory_id DESC
LIMIT 1;

-- lowest record

SELECT * FROM inventory 
order by inventory_id ASC
LIMIT 1;

-- alias in a table 
SELECT * FROM inventory inv

--Display record from one table that has related record from another table 


SELECT 
ord.order_id, 
ord.order_date,
ord.quantity,
cust.name,
inv.product_name 
FROM orders ord 
INNER JOIN customer cust on ord.customer_id = cust.customer_id
INNER JOIN inventory inv on ord.inventory_id = inv.inventory_id;









