WITH cte1 (name_genre, Количество) AS (
    SELECT name_genre, SUM(bb.amount)
    FROM genre g
         JOIN book b USING (genre_id)
         JOIN buy_book bb USING (book_id)
    GROUP BY name_genre)

SELECT name_genre, Количество
FROM cte1
WHERE Количество = (SELECT MIN(Количество) FROM cte1)
