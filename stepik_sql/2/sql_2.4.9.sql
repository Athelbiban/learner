SELECT buy_id, name_client, SUM(bb.amount * price) Стоимость
FROM buy_book bb
    JOIN buy bu USING(buy_id)
    JOIN client c USING(client_id)
    JOIN book bo USING(book_id)
GROUP BY buy_id, name_client
ORDER BY buy_id;
