INSERT INTO book (title, author, price, amount)
SELECT title, author, price, amount
FROM supply
WHERE author NOT IN (
    SELECT author
    FROM book
    );

SELECT * FROM book;

