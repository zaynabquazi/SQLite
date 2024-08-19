-- Record orders 
INSERT INTO orders 
(customer_id, order_date, inventory_id)
VALUES (2, '8/19/2024', 4);  



-- Reduce inventory 
update inventory
set quantity = quantity - 1
where id = 4

-- Print order
SELECT customer.name, inventory.product_name, orders.order_date
FROM orders
INNER JOIN customer ON customer.id = orders.customer_id
INNER JOIN inventory ON inventory.id = orders.inventory_id
WHERE inventory.id = 4;

SELECT * from inventory