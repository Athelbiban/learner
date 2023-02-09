SELECT name_author, title, IF(buy_book.book_id IS NOT NULL, COUNT(title), 0) Количество
FROM author JOIN book USING(author_id) LEFT JOIN buy_book USING(book_id)
GROUP BY book_id, name_author, title
ORDER BY name_author, title;
