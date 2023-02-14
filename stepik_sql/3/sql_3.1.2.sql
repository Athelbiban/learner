SELECT name_student, date_attempt, result
  FROM subject AS su
       JOIN attempt AS a
       ON su.subject_id = a.subject_id
       AND name_subject LIKE 'Основы баз данных'
       JOIN student AS st USING(student_id)
 ORDER BY result DESC;
