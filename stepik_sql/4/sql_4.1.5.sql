--for stepik.org
/*
SELECT author, title, price, amount,
       IF(price > 600, ROUND(price * 0.2, 2), '-') AS sale_20,
       IF(price > 600, ROUND(price * 0.8, 2), '-') AS price_sale
FROM book
ORDER BY author, title;
*/

--for my database
SELECT name_author, title, price, amount,
       IF(price > 600, ROUND(price * 0.2, 2), '-') AS sale_20,
       IF(price > 600, ROUND(price * 0.8, 2), '-') AS price_sale
FROM book b JOIN author a on b.author_id = a.author_id
ORDER BY name_author, title;
