SELECT title Название, author Автор, book.amount + supply.amount Количество
FROM supply INNER JOIN book USING(title, price);
