SELECT name_student, name_subject,
       DATEDIFF(MAX(date_attempt), MIN(date_attempt)) AS Интервал
  FROM student AS s
       JOIN attempt AS a USING(student_id)
       JOIN subject AS su USING(subject_id)
 GROUP BY name_student, name_subject
HAVING COUNT(attempt_id) > 1
 ORDER BY Интервал;
