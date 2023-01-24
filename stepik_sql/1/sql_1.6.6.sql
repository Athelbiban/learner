SELECT name, city, DATEDIFF(date_last, date_first) + 1 AS Длительность
FROM trip
WHERE city NOT IN ('Москва', 'Санкт-Петербург')
ORDER BY Длительность DESC, city DESC;
