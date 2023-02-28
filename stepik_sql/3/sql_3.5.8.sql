SELECT student_name Студент,
       CONCAT(LEFT(step_name, 20), '...') Шаг,
       result Результат,
       FROM_UNIXTIME(submission_time) Дата_отправки,
       SEC_TO_TIME(submission_time - LAG(submission_time, 1, submission_time) OVER(ORDER BY submission_time)) Разница
FROM student s
     JOIN step_student ss on s.student_id = ss.student_id AND student_name LIKE '%61'
     JOIN step s2 on ss.step_id = s2.step_id
