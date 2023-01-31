SELECT name_author, SUM(amount) Количество
FROM author LEFT JOIN book
    USING(author_id)
GROUP BY name_author
HAVING Количество < 10 OR Количество IS NULL
ORDER BY Количество;

