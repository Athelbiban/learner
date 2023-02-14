SELECT name_step, COUNT(buy_id) AS Количество_заказов
  FROM (
       SELECT *
       FROM buy_step
       WHERE date_step_beg AND date_step_end IS NULL
       ) AS query
       RIGHT JOIN step AS s USING(step_id)
 GROUP BY name_step
 ORDER BY name_step;
