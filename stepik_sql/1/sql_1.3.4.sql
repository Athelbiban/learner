SELECT author,
       MIN(price) Минимальная_цена,
       MAX(price) Максимальная_цена,
       AVG(price) Средняя_цена
FROM book
GROUP BY author;

