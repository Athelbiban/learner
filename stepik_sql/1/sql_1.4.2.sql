SELECT author, title, price
FROM book
WHERE price <= (SELECT ROUND(AVG(price), 2) FROM book)
ORDER BY price DESC;

