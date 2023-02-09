SELECT buy_id,
       DATEDIFF(date_step_end, date_step_beg) Количество_дней,
       IF(DATEDIFF(date_step_end, date_step_beg) - days_delivery > 0,
           DATEDIFF(date_step_end, date_step_beg) - days_delivery, 0) Опоздание
FROM city c
    JOIN client cl USING(city_id)
    JOIN buy b USING(client_id)
    JOIN buy_step bs USING(buy_id)
    JOIN step s ON bs.step_id = s.step_id
                AND name_step LIKE 'Транспортировка'
                AND date_step_end IS NOT NULL
