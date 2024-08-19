ALTER TABLE orders
ADD COLUMN inventory_id INTEGER;

ALTER TABLE orders
ADD FOREIGN KEY (inventory_id) REFERENCES inventory(id);
