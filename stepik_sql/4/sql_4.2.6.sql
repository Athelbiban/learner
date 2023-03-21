SELECT title AS Наименование, price AS Цена,
       IF(amount <= 5, 500, 'Бесплатно') AS Стоимость_доставки
FROM book
WHERE price > 600
ORDER BY Цена DESC;
