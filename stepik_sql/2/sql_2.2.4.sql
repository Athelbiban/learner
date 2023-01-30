SELECT name_city, name_author, DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND() * 365) DAY) Дата
FROM author CROSS JOIN city
ORDER BY name_city, Дата DESC;

