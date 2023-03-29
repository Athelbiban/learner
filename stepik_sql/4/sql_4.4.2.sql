INSERT INTO attempt (student_id, subject_id, date_attempt)
SELECT student_id, subject_id, CURRENT_DATE
FROM attempt
GROUP BY student_id, subject_id
HAVING MAX(result) < 70 AND COUNT(student_id) < 3
