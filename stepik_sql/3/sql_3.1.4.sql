SELECT name_student, result
  FROM student AS s
       JOIN attempt AS a
       ON s.student_id = a.student_id
       AND result = (
             SELECT result
               FROM student
                    JOIN attempt USING(student_id)
              ORDER BY result DESC
              LIMIT 1)
 ORDER BY name_student;
