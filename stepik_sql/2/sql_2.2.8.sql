SELECT title, name_author, name_genre, price, amount
FROM author INNER JOIN book USING(author_id) INNER JOIN genre USING(genre_id)
GROUP BY title, name_author, name_genre, price, amount, genre.genre_id
HAVING genre.genre_id IN (
      SELECT q.genre_id
      FROM (
            SELECT genre_id, SUM(amount) amount_sum
            FROM book
            GROUP BY genre_id) q
            INNER JOIN
           (
            SELECT genre_id, SUM(amount) amount_sum
            FROM book
            GROUP BY genre_id
            ORDER BY amount_sum DESC
            LIMIT 1) p
            USING (amount_sum))
ORDER BY title;

