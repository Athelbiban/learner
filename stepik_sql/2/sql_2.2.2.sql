SELECT title, name_genre, price
FROM genre INNER JOIN book
    ON genre.genre_id = book.genre_id
WHERE amount > 8
ORDER BY price DESC;
