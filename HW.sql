-- print customer details (Jane Smith)
SELECT name FROM Customer 
WHERE customer_id = 2;

-- print what customer has purchased (Jane Smith)
SELECT 
cust.name,
inv.product_name 
FROM orders ord 
INNER JOIN customer cust on ord.customer_id = cust.customer_id
INNER JOIN inventory inv on ord.inventory_id = inv.inventory_id

WHERE cust.customer_id = 2;

-- print all orders (product name, customer name, quantity, order date) 
SELECT 
inventory.product_name, 
customer.name,
orders.quantity, 
orders.order_date
FROM orders 
INNER JOIN customer  on orders.customer_id = customer.customer_id
INNER JOIN inventory  on orders.inventory_id = inventory.inventory_id;


-- print which item sold the most and product name 
SELECT inventory.product_name, Max(orders.quantity) AS total_quantity
FROM orders 
INNER JOIN inventory ON orders.inventory_id = inventory.inventory_id
GROUP BY orders.inventory_id
LIMIT 1;

-- insert some records in all tables 
INSERT INTO customer (customer_id, name, email) VALUES (11, 'KAKA HEAD', 'iLoveToHagu@example.com');
INSERT INTO inventory (inventory_id, product_name, quantity) VALUES (11, 'Tums', 50);
INSERT INTO orders (order_id, customer_id, order_date) VALUES (10, 6, '8/19/2024');



-- update random data in all tables 
UPDATE orders 
SET order_date = '8/19/2024' 
WHERE order_id = 11;

--reduce an item from the inventory

