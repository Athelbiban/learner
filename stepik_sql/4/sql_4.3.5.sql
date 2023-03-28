SELECT name_author, name_genre, COUNT(title) AS Количество
FROM (author, genre)
     LEFT JOIN book b USING(genre_id, author_id)
GROUP BY name_author, name_genre
ORDER BY name_author, Количество DESC, name_genre
