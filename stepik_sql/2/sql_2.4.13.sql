SELECT name_genre, SUM(bb.amount) Количество
FROM genre g
    JOIN book b USING(genre_id)
    JOIN buy_book bb USING(book_id)
GROUP BY name_genre
HAVING SUM(bb.amount) = (
    SELECT MAX(sum_amount) max_amount
    FROM (
        SELECT SUM(bb.amount) sum_amount
        FROM genre g
            JOIN book b USING(genre_id)
            JOIN buy_book bb USING(book_id)
        GROUP BY name_genre) q);
