WITH cte1 AS
(SELECT module_id, lesson_id,
        CONCAT(module_id, '.', lesson_position, ' ', lesson_name) AS Урок,
        SUM(submission_time - attempt_time) AS lesson_time
FROM module m
     JOIN lesson l USING(module_id)
     JOIN step s USING(lesson_id)
     JOIN step_student USING(step_id)
WHERE SEC_TO_TIME(submission_time - attempt_time) < '04:00:00'
GROUP BY lesson_id, student_id)

SELECT ROW_NUMBER() OVER(ORDER BY AVG(lesson_time)) AS Номер,
       Урок,
       ROUND(AVG(lesson_time / 3600), 2) AS Среднее_время
FROM cte1
GROUP BY Урок
