SELECT title, author, price, amount,
    (SELECT MAX(price) FROM book) - price наценка,
    ROUND(((SELECT MAX(price) FROM book) - price) * 100 / (SELECT MAX(price) FROM book)) процент_скидки
FROM book
WHERE (SELECT MAX(price) FROM book) != price;

