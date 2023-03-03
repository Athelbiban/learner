WITH cte1 (st_name, lesson, sub_time)
    AS (SELECT student_name,
               CONCAT(module_id, '.', lesson_position),
               FROM_UNIXTIME(submission_time)
          FROM student s
                   JOIN step_student ss ON s.student_id = ss.student_id
                   AND result = 'correct'
                   JOIN step st USING (step_id)
                   JOIN lesson l USING (lesson_id)
         GROUP BY student_name, module_id, lesson_position
         ORDER BY student_name),

    cte2 (student)
        AS (SELECT st_name
            FROM (SELECT st_name, COUNT(lesson) AS count_lesson
                  FROM cte1
                  GROUP BY st_name) AS q
            WHERE count_lesson = 3)

SELECT *
FROM cte1
WHERE st_name IN (SELECT * FROM cte2)
