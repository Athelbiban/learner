SELECT DISTINCT name_client
FROM author a
    JOIN book b ON a.author_id = b.author_id AND name_author LIKE 'Достоевский%'
    JOIN buy_book bb USING(book_id)
    JOIN buy bu USING(buy_id)
    JOIN client c USING(client_id)
ORDER BY name_client;
