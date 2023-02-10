SELECT title
FROM book b
    LEFT JOIN buy_book bb ON b.book_id = bb.book_id
WHERE buy_book_id IS NULL
ORDER BY title;
