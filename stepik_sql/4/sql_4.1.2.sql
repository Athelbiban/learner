WITH cte1 AS (
    SELECT CASE
           WHEN price < 600 THEN 0
           WHEN price BETWEEN 600 AND 700 THEN 600
           ELSE 700
           END AS beg_range,
           CASE
           WHEN price < 600 THEN 600
           WHEN price BETWEEN 600 AND 700 THEN 700
           ELSE 10000
           END AS end_range,
           price,
           amount
    FROM book)

SELECT beg_range, end_range,
       ROUND(AVG(price), 2) AS Средняя_цена,
       ROUND(SUM(price * amount), 2) AS Стоимость,
       COUNT(price) AS Количество
FROM cte1
GROUP BY beg_range, end_range
ORDER BY beg_range;
