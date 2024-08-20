ALTER TABLE orders
ADD COLUMN inventory_id INTEGER;

ALTER TABLE orders
ADD FOREIGN KEY (inventory_id) REFERENCES inventory(id);

--alter customers table 

ALTER TABLE customer 
RENAME COLUMN ID TO customer_id;

--alter inventory table 

ALTER TABLE inventory 
RENAME COLUMN id to inventory_id;

--alter orders table 

ALTER TABLE orders 
RENAME COLUMN id to order_id 

