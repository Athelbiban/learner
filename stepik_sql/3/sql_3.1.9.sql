SELECT name_student, name_subject, date_attempt, ROUND(AVG(is_correct) * 100, 2) AS Результат
FROM student AS st
     JOIN attempt AS a ON st.student_id = a.student_id
     JOIN subject AS su ON su.subject_id = a.subject_id
     JOIN testing AS t ON a.attempt_id = t.attempt_id
     JOIN answer AS an ON t.answer_id = an.answer_id
GROUP BY t.attempt_id
ORDER BY name_student, date_attempt DESC;
