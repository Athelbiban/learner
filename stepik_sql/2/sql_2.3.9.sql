INSERT INTO author (name_author)
SELECT author
FROM author a RIGHT JOIN supply s ON a.name_author = s.author
WHERE name_author IS NULL;

INSERT INTO book (title, author_id, price, amount)
SELECT s.title, au.author_id, s.price, s.amount
FROM author a
    JOIN book b USING(author_id)
    RIGHT JOIN supply s ON a.name_author = s.author AND b.title = s.title
    JOIN author au ON s.author = au.name_author
WHERE b.title IS NULL;

UPDATE book
SET genre_id = (
    CASE
    WHEN title = 'Доктор Живаго' THEN 1
    WHEN title = 'Стихотворения и поэмы' THEN 2
    WHEN title = 'Остров сокровищ' THEN 3
    END)
WHERE genre_id IS NULL;

UPDATE book b JOIN (
    SELECT genre_id, ROUND(AVG(price), 2) new_price
    FROM book
    GROUP BY genre_id
    ) q USING(genre_id)
SET price = new_price;

SELECT * FROM book;
