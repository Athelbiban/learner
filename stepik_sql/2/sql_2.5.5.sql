UPDATE book AS b
       JOIN buy_book as bb
       ON b.book_id = bb.book_id
           AND buy_id = 5
   SET b.amount = b.amount - bb.amount;

SELECT * FROM book;
