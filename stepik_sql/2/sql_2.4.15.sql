SELECT title, SUM(sum_amount) Количество, SUM(price * sum_amount) Сумма
FROM (
    SELECT title, SUM(ba.amount) sum_amount, ba.price
    FROM buy_archive ba
             JOIN book b USING(book_id)
    GROUP BY title, ba.price
    UNION
    SELECT title, SUM(bb.amount) sum_amount, price
    FROM step s
             JOIN buy_step bs ON s.step_id = bs.step_id AND s.name_step = 'Оплата' AND bs.date_step_end
             JOIN buy_book bb USING(buy_id)
             JOIN book b USING(book_id)
    GROUP BY title, price) query
GROUP BY title
ORDER BY Сумма DESC
