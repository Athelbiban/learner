SELECT author,
       COUNT(amount) Количество_произведений,
       MIN(price) Минимальная_цена,
       SUM(amount) Число_книг
FROM book
WHERE price > 500 AND amount > 1
GROUP BY author
HAVING COUNT(title) >= 2;

