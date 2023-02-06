DELETE FROM genre
WHERE genre_id IN (
    SELECT genre_id
    FROM book
    GROUP BY genre_id
    HAVING COUNT(title) < 4 AND COUNT(author_id) < 4);

SELECT * FROM book;

SELECT * FROM genre;
