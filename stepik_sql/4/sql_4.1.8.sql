SELECT author,
       COUNT(title) AS Количество_произведений,
       MIN(price) AS Минимальная_цена,
       SUM(amount) AS Число_книг
FROM book
GROUP BY author
HAVING Количество_произведений > 1 AND MAX(IF(amount > 1, price, NULL)) > 500
ORDER BY author;
