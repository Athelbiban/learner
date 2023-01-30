SELECT name_genre
FROM genre LEFT JOIN book USING(genre_id)
WHERE title IS NULL;

