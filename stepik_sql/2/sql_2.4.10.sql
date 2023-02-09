SELECT buy_id, name_step
FROM step s
    JOIN buy_step b
        ON s.step_id = b.step_id
        AND date_step_beg
        AND date_step_end IS NULL
ORDER BY buy_id;
