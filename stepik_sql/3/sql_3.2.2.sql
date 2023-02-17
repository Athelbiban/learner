INSERT INTO attempt (student_id, subject_id, date_attempt)
SELECT st.student_id, s.subject_id, CURDATE()
FROM student AS st
     JOIN attempt AS a
     ON st.student_id = a.student_id
     AND name_student LIKE 'Баранов П%'
     JOIN subject s
     ON a.subject_id = s.subject_id
     AND name_subject = 'Основы баз данных';

SELECT * FROM attempt;
