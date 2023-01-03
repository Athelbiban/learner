UPDATE book SET author='Дарья Донцова';
SELECT author, concat('Евлампия романова и ',title) AS title, ROUND(price * 1.42, 2) AS price FROM book
ORDER BY price DESC, title DESC;
