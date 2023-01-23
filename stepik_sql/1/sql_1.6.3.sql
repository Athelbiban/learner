SELECT name
FROM trip
WHERE city = 'Москва'
GROUP BY name
ORDER BY name;
