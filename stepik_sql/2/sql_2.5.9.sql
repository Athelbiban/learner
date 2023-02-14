UPDATE buy_step AS bs
       JOIN step AS s
       ON bs.step_id = s.step_id
           AND buy_id = 5
           AND name_step = 'Оплата'
SET date_step_beg = '2020-04-12';
