SET @total_step = (SELECT COUNT(DISTINCT step_id) FROM step_student);

WITH cte
    AS (SELECT student_id,
               ROUND(COUNT(DISTINCT step_id) / @total_step * 100) AS Прогресс
          FROM step_student
         WHERE result = 'correct'
      GROUP BY student_id)

SELECT student_name AS Студент,
       Прогресс,
       CASE
       WHEN Прогресс < 80 THEN ''
       WHEN Прогресс = 100 THEN 'Сертификат с отличием'
       ELSE 'Сертификат'
       END AS Результат
  FROM cte c
       JOIN student s ON c.student_id = s.student_id
 ORDER BY Прогресс DESC, Студент;
