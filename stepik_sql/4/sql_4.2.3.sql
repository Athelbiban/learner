CREATE TABLE store
    WITH cte1 AS (
        SELECT * FROM book
        UNION ALL
        SELECT * FROM supply)

    SELECT title, author, MAX(price) AS price, SUM(amount) AS amount
    FROM cte1
    GROUP BY title, author
    HAVING SUM(amount) > (SELECT AVG(amount) FROM cte1)
    ORDER BY author, price DESC;

SELECT * FROM store;
