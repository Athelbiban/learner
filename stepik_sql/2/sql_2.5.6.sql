DROP TABLE IF EXISTS buy_pay;

CREATE TABLE IF NOT EXISTS buy_pay
SELECT title, name_author, price, bb.amount, bb.amount * price AS Стоимость
  FROM buy_book AS bb
       INNER JOIN book AS b
       ON bb.book_id = b.book_id
           AND buy_id = 5
       INNER JOIN author AS a
       USING(author_id)
 ORDER BY title;

SELECT * FROM buy_pay;
