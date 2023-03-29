SET @last_order = (SELECT buy_id
                   FROM client c
                        JOIN buy b ON c.client_id = b.client_id
                        AND name_client LIKE 'Баранов%'
                   ORDER BY buy_id DESC
                   LIMIT 1);

INSERT INTO buy_book (buy_id, book_id, amount)
SELECT @last_order, book_id, 1
FROM book b
     JOIN author a ON b.author_id = a.author_id
     AND name_author LIKE 'Достоевский%';
