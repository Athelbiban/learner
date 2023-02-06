DELETE FROM author
WHERE author_id IN (
    SELECT author_id
    FROM book
    GROUP BY author_id
    HAVING SUM(amount) < 20);

SELECT * FROM author;

SELECT * FROM book;
