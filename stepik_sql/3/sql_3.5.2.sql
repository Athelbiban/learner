SET @length_str = 16;

SELECT IF(LENGTH(CONCAT(m.module_id, ' ', module_name)) >= @length_str,
            CONCAT(LEFT(CONCAT(m.module_id, ' ', module_name), @length_str), '...'),
                CONCAT(m.module_id, ' ', module_name)) AS Модуль,
       IF(LENGTH(CONCAT(m.module_id, '.', l.lesson_position, ' ', lesson_name)) >= @length_str,
            CONCAT(LEFT(CONCAT(m.module_id, '.', l.lesson_position, ' ', lesson_name), @length_str), '...'),
                CONCAT(m.module_id, '.', l.lesson_position, ' ', lesson_name)) AS Урок,
       CONCAT(m.module_id, '.', l.lesson_position, '.', s.step_position, ' ', step_name) AS Шаг
  FROM step s
       JOIN lesson l on s.lesson_id = l.lesson_id
       AND step_name LIKE '%вложен% запрос%'
       JOIN module m on l.module_id = m.module_id
 ORDER BY Шаг;
