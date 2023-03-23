SELECT author, title,
       price DIV 1 AS Рубли,
       ROUND(MOD(price, 1) * 100) AS Копейки
FROM book
ORDER BY Копейки DESC;
