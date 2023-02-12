DROP TABLE IF EXISTS buy_pay;

CREATE TABLE IF NOT EXISTS buy_pay
SELECT buy_id, SUM(bb.amount) AS Количество, SUM(price * bb.amount) AS Итого
  FROM book AS b
       INNER JOIN buy_book AS bb
       ON b.book_id = bb.book_id
           AND buy_id = 5
 GROUP BY buy_id;

SELECT * FROM buy_pay;
