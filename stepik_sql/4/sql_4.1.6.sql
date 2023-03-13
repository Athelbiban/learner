SET @avg_price = (SELECT AVG(price) FROM book);

SELECT author, SUM(price * amount) AS Стоимость
FROM book
GROUP BY author
HAVING MAX(price) > @avg_price
ORDER BY Стоимость DESC;
