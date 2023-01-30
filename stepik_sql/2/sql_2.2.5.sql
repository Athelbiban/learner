SELECT name_genre, title, name_author
FROM author
    JOIN book USING(author_id)
    JOIN genre USING(genre_id)
WHERE name_genre RLIKE '%? ?%?роман%? ?%?'
ORDER BY title;

