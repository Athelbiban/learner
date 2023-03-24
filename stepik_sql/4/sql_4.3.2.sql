SELECT CONCAT('Графоман и ', author) AS Автор,
       CONCAT(title, '. Краткое содержание.') AS Название,
       IF(price * 0.4 > 250, 250, price * 0.4) AS Цена,
       CASE
           WHEN amount <= 3 THEN 'высокий'
           WHEN amount > 10 THEN 'низкий'
           ELSE 'средний'
       END AS Спрос,
       CASE
           WHEN amount <= 2 THEN 'очень мало'
           WHEN amount >= 15 THEN 'много'
           ELSE 'в наличии'
           END AS Наличие
FROM book
ORDER BY Цена, amount, Название;
