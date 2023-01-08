SELECT
    MIN(price) Минимальная_цена,
    MAX(price) Максимальная_цена,
    ROUND(AVG(price), 2) Средняя_цена
FROM book;

