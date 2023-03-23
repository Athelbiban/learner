SELECT author, title, amount,
       price AS real_price,
       ROUND(IF(amount * price > 5000, price * 1.2, price * 0.8), 2) AS new_price,
       CASE
           WHEN price < 500 THEN 99.99
           WHEN amount < 5 AND price > 500 THEN 149.99
           ELSE 0
       END AS delivery_price
FROM book
WHERE author REGEXP '(Булгаков|Есенин)' AND amount BETWEEN 3 AND 14
ORDER BY author, title DESC, delivery_price;
