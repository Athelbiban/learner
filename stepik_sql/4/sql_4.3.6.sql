SELECT author AS Автор, title AS Название_книги, price AS Цена,
       CASE
           WHEN price <= 600 THEN 'ручка'
           WHEN price > 700 THEN 'гороскоп'
           ELSE 'детская раскраска'
           END AS Подарок
FROM book
WHERE price >= 500
ORDER BY author, title;
