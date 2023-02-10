SELECT YEAR(date_payment) Год, MONTHNAME(date_payment) Месяц, SUM(price * amount) Сумма
FROM (
    SELECT date_payment, price, amount
    FROM buy_archive
    UNION
    SELECT date_step_end, price, buy_book.amount
    FROM step
        JOIN buy_step ON buy_step.step_id = step.step_id AND date_step_end AND name_step LIKE 'Оплата'
        JOIN buy_book USING(buy_id)
        JOIN book USING(book_id)) query
GROUP BY Месяц, Год
ORDER BY Месяц, Год;
