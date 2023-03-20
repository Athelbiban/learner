SELECT author, title,
       CASE
           WHEN price < 500 THEN 'низкая'
           WHEN price > 700 THEN 'высокая'
           ELSE 'средняя'
       END AS price_category,
       price * amount AS cost
FROM book
WHERE author NOT LIKE 'Есенин%' AND title <> 'Белая гвардия'
ORDER BY cost DESC, title;
