-- SQLite
select * from phonenumbers;
select * from phonenumbers where phonenumber like '%555%';
select * from phonenumbers where phonenumber like '%555%' and phonenumber like '%555%'; 


SELECT phonenumber, COUNT(*)
FROM phonenumbers
WHERE phonenumber LIKE '%555%'
GROUP BY phonenumber;