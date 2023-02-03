UPDATE book b
    INNER JOIN author a USING(author_id)
    INNER JOIN supply s ON a.name_author = s.author
    AND b.title = s.title
SET b.price = (b.price * b.amount + s.price * s.amount) / (b.amount + s.amount),
    b.amount = b.amount + s.amount,
    s.amount = 0
WHERE b.price <> s.price;

SELECT * FROM book;

SELECT * FROM supply;
