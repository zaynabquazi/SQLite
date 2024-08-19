-- SQLite
SELECT * FROM Location;

SELECT * From PhoneBook;

SELECT People, Number FROM PhoneBook
WHERE Location = 'Los Angeles, CA';

SELECT count(*) FROM PhoneBook

SELECT * FROM PhoneBook 
WHERE Mobile IS NULL;

-- Select for Customer: 

SELECT * FROM Customer;

-- Select for Inventory: 

SELECT * FROM inventory;

-- Select for Orders: 

SELECT * FROM orders; 