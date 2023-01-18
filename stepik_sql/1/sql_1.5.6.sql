UPDATE book
SET price = price * 0.9
WHERE amount BETWEEN 5 AND 10;

SELECT * FROM book;

