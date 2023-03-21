SET @max_price = (SELECT MAX(price * amount) FROM book);

SELECT title, author, amount,
       IF(amount % 2 = 0, NULL, ROUND(@max_price - price * amount, 2)) AS Разница_с_макс_стоимостью
FROM book
HAVING Разница_с_макс_стоимостью IS NOT NULL
ORDER BY Разница_с_макс_стоимостью DESC;
