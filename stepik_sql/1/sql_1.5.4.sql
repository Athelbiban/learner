INSERT INTO book (title, author, price, amount)
SELECT title, author, price, amount
FROM supply
WHERE author NOT IN ('Достоевский Ф.М.', 'Булгаков М.А.');

SELECT * FROM book;

