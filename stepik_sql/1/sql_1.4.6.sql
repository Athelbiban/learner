SELECT title, author, amount, (
    SELECT MAX(amount)
    FROM book
    ) - amount Заказ
FROM book
WHERE (
    SELECT MAX(amount)
    FROM book
    ) - amount > 0;

