SET @sale = NULL;

SELECT author, title, amount, price,
       CONCAT(CASE
                  WHEN amount >= 5 THEN @sale := 50
                  WHEN price >= 700 THEN @sale := 20
                  ELSE @sale := 10
              END, '%') AS Скидка,
       ROUND(price * (100 - @sale) / 100, 2) AS Цена_со_скидкой
FROM book;
