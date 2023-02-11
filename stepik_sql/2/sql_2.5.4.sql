INSERT INTO buy_book (buy_id, book_id, amount)
SELECT 5, book_id, 2
  FROM author AS a
       JOIN book AS b
       ON a.author_id = b.author_id
           AND name_author LIKE 'Пастернак%'
           AND title = 'Лирика';

INSERT INTO buy_book (buy_id, book_id, amount)
SELECT 5, book_id, 1
  FROM author AS a
       JOIN book AS b
       ON a.author_id = b.author_id
           AND name_author LIKE 'Булгаков%'
           AND title = 'Белая гвардия';

SELECT * FROM buy_book;
