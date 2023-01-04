SELECT title, author, amount,
    ROUND(price - price*30/100, 2) AS new_price
FROM book;
