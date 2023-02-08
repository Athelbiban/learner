SELECT buy_id, date_step_end
FROM step s JOIN buy_step bs USING(step_id)
WHERE name_step = 'Оплата' AND date_step_end IS NOT NULL;
