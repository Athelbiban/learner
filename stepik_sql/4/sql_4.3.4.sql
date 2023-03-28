SET @revenue = (SELECT SUM(price * amount) FROM book);

SELECT author, title, price, amount, ROUND(price * amount / @revenue * 100, 2) AS income_percent
FROM book
ORDER BY income_percent DESC;
