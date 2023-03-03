WITH cte1 (st_name, lesson, sub_time)
    AS (SELECT student_name,
               CONCAT(module_id, '.', lesson_position),
               MAX(submission_time)
        FROM student s
             JOIN step_student ss ON s.student_id = ss.student_id
             AND result = 'correct'
             JOIN step st USING (step_id)
             JOIN lesson l USING (lesson_id)
        GROUP BY student_name, module_id, lesson_position
        ORDER BY student_name),

cte2 AS (SELECT st_name
         FROM cte1
         GROUP BY st_name
         HAVING COUNT(lesson) = 3)

SELECT c1.st_name AS Студент,
       lesson AS Урок,
       FROM_UNIXTIME(sub_time) AS Макс_время_отправки,
       IFNULL(CEIL(
           (sub_time - LAG(sub_time) OVER(PARTITION BY c1.st_name ORDER BY sub_time))
               / 86400), '-') AS Интервал
FROM cte1 c1 JOIN cte2 c2 USING(st_name)
