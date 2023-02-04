INSERT INTO book (title, author_id, price, amount)
SELECT title, author_id, price, amount
FROM supply s JOIN author a ON s.author = a.name_author
WHERE amount <> 0;

SELECT * FROM book;
