SELECT name_author, name_genre, COUNT(title) Количество
FROM genre INNER JOIN author LEFT JOIN book USING(genre_id, author_id)
GROUP BY name_genre, name_author
ORDER BY name_author, Количество DESC;
