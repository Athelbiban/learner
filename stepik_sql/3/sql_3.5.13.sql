WITH cte1 AS (
    SELECT student_name, step_id, result,
           LEAD(result) OVER (PARTITION BY student_name, step_id ORDER BY student_name, step_id, submission_time) 
               AS lead_result
    FROM student s JOIN step_student ss ON s.student_id = ss.student_id),

    cte2 AS (
    SELECT student_name, step_id, COUNT(result) AS count_result
    FROM student s JOIN step_student ss ON s.student_id = ss.student_id AND result = 'correct'
    GROUP BY student_name, step_id
    HAVING count_result > 1
    ORDER BY student_name, step_id),
    cte3 AS (
    SELECT student_name, step_id
    FROM student s JOIN step_student ss ON s.student_id = ss.student_id
    GROUP BY student_name, step_id
    HAVING COUNT(step_id) = SUM(IF(result = 'wrong', 1, 0))
    ORDER BY student_name, step_id)

SELECT 'I' AS Группа, student_name AS Студент, COUNT(student_name) AS Количество_шагов
FROM cte1
WHERE result = 'correct' AND lead_result = 'wrong'
GROUP BY student_name
UNION ALL
SELECT 'II' AS Группа, student_name AS Студент, COUNT(student_name) AS Количество_шагов
FROM cte2
GROUP BY student_name
UNION ALL
SELECT 'III' AS Группа, student_name AS Студент, COUNT(student_name) AS Количество_шагов
FROM cte3
GROUP BY student_name
ORDER BY Группа, Количество_шагов DESC, Студент
