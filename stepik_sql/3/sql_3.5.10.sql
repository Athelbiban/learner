WITH get_count_step(Модуль, Студент, Пройдено_шагов) AS (
         SELECT module_id, student_name,
                COUNT(DISTINCT s.step_id) count_step
         FROM step s
              JOIN step_student ss ON s.step_id = ss.step_id
              AND result = 'correct'
              JOIN lesson l USING(lesson_id)
              JOIN student st USING(student_id)
         GROUP BY module_id, student_id)

SELECT Модуль, Студент, Пройдено_шагов,
       ROUND(Пройдено_шагов /
                MAX(Пройдено_шагов) OVER (PARTITION BY Модуль) * 100, 1)
                    AS Относительный_рейтинг
FROM get_count_step
ORDER BY Модуль, Относительный_рейтинг DESC, Студент
