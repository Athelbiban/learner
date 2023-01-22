/*
Условие задачи:
Делаем скидку 5% на самое большое количество экземпляров книг (Стихи Есенина), чтобы поскорее расходились.
*/

--Первое решение
UPDATE book, (SELECT MAX(amount) AS max_amount FROM book) AS add_table
SET price = ROUND(price * 0.95, 2)
WHERE amount = add_table.max_amount;

SELECT * FROM book;

--Второе решение
/*
SELECT author, title, amount,
    ROUND(IF(amount = (SELECT MAX(amount) FROM book), price * 0.95, price), 2) AS new_price
FROM book;
*/
