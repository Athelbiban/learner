SET @avg_sum = (SELECT AVG(s)
                FROM (SELECT SUM(price * bb.amount) AS s
                      FROM buy_book bb
                           JOIN book b USING(book_id)
                           JOIN buy b2 USING(buy_id)
                      GROUP BY client_id) q);

SELECT name_client,
       SUM(price * bb.amount) AS Общая_сумма_заказов,
       COUNT(DISTINCT buy_id) AS Заказов_всего,
       SUM(bb.amount) AS Книг_всего
FROM client c
     JOIN buy b USING(client_id)
     JOIN buy_book bb USING(buy_id)
     JOIN book b2 USING(book_id)
GROUP BY name_client
HAVING Общая_сумма_заказов > @avg_sum
ORDER BY name_client;
