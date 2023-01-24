SELECT city, COUNT(city) AS Количество
FROM trip
GROUP BY city
ORDER BY Количество DESC
LIMIT 2;

