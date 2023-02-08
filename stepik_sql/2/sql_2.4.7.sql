SELECT name_city, COUNT(city_id) Количество
FROM buy b JOIN client cl USING(client_id) LEFT JOIN city c USING(city_id)
GROUP BY name_city
ORDER BY Количество DESC, name_city;
