SELECT buy.buy_id, book.title, book.price, buy_book.amount
  FROM client
      JOIN buy USING(client_id)
      JOIN buy_book USING(buy_id)
      JOIN book USING(book_id)
 WHERE name_client = 'Баранов Павел'
ORDER BY buy_id, title;
