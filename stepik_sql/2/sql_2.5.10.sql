UPDATE buy_step AS bs
       JOIN step AS s USING(step_id)
   SET date_step_end = '2020-04-13'
 WHERE buy_id = 5
       AND name_step = 'Оплата';

UPDATE buy_step AS bs
       JOIN step AS s USING(step_id)
   SET date_step_beg = '2020-04-13'
 WHERE buy_id = 5
       AND name_step = 'Упаковка';

SELECT * FROM buy_step;
