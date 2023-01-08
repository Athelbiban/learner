SELECT
    ROUND(AVG(price), 2) Средняя_цена,
    SUM(price * amount) Стоимость
FROM book
WHERE amount BETWEEN 5 AND 14;

