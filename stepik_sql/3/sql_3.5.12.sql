SET @sec_per_hour = 3600;
SET @avg_time = (
    SELECT ROUND(AVG(IF(submission_time - attempt_time <= @sec_per_hour, submission_time - attempt_time, NULL)))
    FROM step_student ss
         JOIN student s ON ss.student_id = s.student_id AND student_name LIKE '%59');

WITH cte1 AS (
SELECT student_name AS Студент,
       CONCAT(module_id, '.', lesson_position, '.', step_position) AS Шаг,
       result AS Результат,
       IF(submission_time - attempt_time <= @sec_per_hour, submission_time - attempt_time, @avg_time) AS at_time,
       submission_time, step_id
FROM student s
     JOIN step_student ss ON s.student_id = ss.student_id AND student_name LIKE '%59'
     JOIN step s2 USING(step_id)
     JOIN lesson l USING(lesson_id)
ORDER BY submission_time)

SELECT Студент, Шаг,
       ROW_NUMBER() OVER(PARTITION BY step_id ORDER BY submission_time) AS Номер_попытки,
       Результат, SEC_TO_TIME(at_time) AS Время_попытки,
       ROUND(at_time / SUM(at_time) OVER (PARTITION BY step_id) * 100, 2) AS Относительное_время
FROM cte1
