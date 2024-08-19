-- TestDataForPerson 
-- Persons 

INSERT INTO "Person" ("Name", "Key") VALUES ('John Doe', 1);
INSERT INTO "Person" ("Name", "Key") VALUES ('Jane Smith', 2);
INSERT INTO "Person" ("Name", "Key") VALUES ('Michael Johnson', 3);
INSERT INTO "Person" ("Name", "Key") VALUES ('Emily Davis', 4);
INSERT INTO "Person" ("Name", "Key") VALUES ('David Martinez', 5);
INSERT INTO "Person" ("Name", "Key") VALUES ('Laura Wilson', 6);
INSERT INTO "Person" ("Name", "Key") VALUES ('James Brown', 7);
INSERT INTO "Person" ("Name", "Key") VALUES ('Sophia Taylor', 8);
INSERT INTO "Person" ("Name", "Key") VALUES ('Daniel Harris', 9);
INSERT INTO "Person" ("Name", "Key") VALUES ('Olivia Lewis', 10);

-- Cutomers : 
INSERT INTO customer (id, name, email) VALUES (1, 'John Doe', 'johndoe@example.com');
INSERT INTO customer (id, name, email) VALUES (2, 'Jane Smith', 'janesmith@example.com');
INSERT INTO customer (id, name, email) VALUES (3, 'Alice Johnson', 'alicej@example.com');
INSERT INTO customer (id, name, email) VALUES (4, 'Bob Brown', 'bobbrown@example.com');
INSERT INTO customer (id, name, email) VALUES (5, 'Charlie Davis', 'charlied@example.com');
INSERT INTO customer (id, name, email) VALUES (6, 'Emily White', 'emilyw@example.com');
INSERT INTO customer (id, name, email) VALUES (7, 'Frank Green', 'frankg@example.com');
INSERT INTO customer (id, name, email) VALUES (8, 'Grace Black', 'graceb@example.com');
INSERT INTO customer (id, name, email) VALUES (9, 'Henry Walker', 'henryw@example.com');
INSERT INTO customer (id, name, email) VALUES (10, 'Isabel Young', 'isabely@example.com');

-- Inventory : 

INSERT INTO inventory (id, product_name, quantity) VALUES (1, 'Laptop', 50);
INSERT INTO inventory (id, product_name, quantity) VALUES (2, 'Smartphone', 120);
INSERT INTO inventory (id, product_name, quantity) VALUES (3, 'Tablet', 75);
INSERT INTO inventory (id, product_name, quantity) VALUES (4, 'Headphones', 200);
INSERT INTO inventory (id, product_name, quantity) VALUES (5, 'Keyboard', 150);
INSERT INTO inventory (id, product_name, quantity) VALUES (6, 'Mouse', 180);
INSERT INTO inventory (id, product_name, quantity) VALUES (7, 'Monitor', 90);
INSERT INTO inventory (id, product_name, quantity) VALUES (8, 'Printer', 40);
INSERT INTO inventory (id, product_name, quantity) VALUES (9, 'Webcam', 110);
INSERT INTO inventory (id, product_name, quantity) VALUES (10, 'Charger', 250);

-- Orders : 

INSERT INTO orders (id, customer_id, order_date) VALUES (1, 1, '2024-08-01');
INSERT INTO orders (id, customer_id, order_date) VALUES (2, 2, '2024-08-02');
INSERT INTO orders (id, customer_id, order_date) VALUES (3, 3, '2024-08-03');
INSERT INTO orders (id, customer_id, order_date) VALUES (4, 4, '2024-08-04');
INSERT INTO orders (id, customer_id, order_date) VALUES (5, 1, '2024-08-05');
INSERT INTO orders (id, customer_id, order_date) VALUES (6, 2, '2024-08-06');
INSERT INTO orders (id, customer_id, order_date) VALUES (7, 3, '2024-08-07');
INSERT INTO orders (id, customer_id, order_date) VALUES (8, 4, '2024-08-08');
INSERT INTO orders (id, customer_id, order_date) VALUES (9, 5, '2024-08-09');
INSERT INTO orders (id, customer_id, order_date) VALUES (10, 6, '2024-08-10');

