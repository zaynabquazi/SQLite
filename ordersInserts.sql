SELECT * FROM customer; 

SELECT * from inventory;

SELECT * FROM orders;

INSERT INTO orders 
(customer_id, order_date, inventory_id)
VALUES(1, '8/19/2024', 1);

SELECT customer.name, inventory.product_name, orders.order_date
FROM orders
INNER JOIN customer ON customer.id = orders.customer_id
INNER JOIN inventory ON inventory.id = orders.inventory_id;

INSERT INTO orders
(customer_id, order_date, inventory_id) 
VALUES (1, '8/19/2024', 3);

SELECT customer_id, inventory.product_name,orders.order_date
FROM orders 
INNER JOIN customer on customer.id = orders.customer_id
INNER JOIN inventory on inventory.id = orders.inventory_id;


UPDATE orders 
SET quantity = 1 






