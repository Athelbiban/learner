SELECT amount, COUNT(title) c
FROM book
GROUP BY amount
HAVING c = 1

