SELECT author AS Автор,
       MIN(amount) Наименьшее_кол_во,
       MAX(amount) Наибольшее_кол_во
FROM book
GROUP BY author
HAVING SUM(amount) < 10
