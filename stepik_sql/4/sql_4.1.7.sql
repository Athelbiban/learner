SELECT author AS Автор,
       title AS Название_книги,
       amount AS Количество,
       price AS Розничная_цена,
       IF(amount >= 10, 15, 0) AS Скидка,
       ROUND(price * (1 - (SELECT Скидка) / 100), 2) AS Оптовая_цена
--       IF(amount >= 10, ROUND(price * 0.85, 2), price) AS Оптовая_цена
FROM book
ORDER BY Автор, Название_книги;
