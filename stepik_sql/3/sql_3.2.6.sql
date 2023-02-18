INSERT INTO student
SET name_student = 'Востров Стас';

INSERT INTO attempt (student_id, subject_id, date_attempt, result)
SELECT student_id,
       subject_id,
       DATE_ADD(CURDATE(), interval -(ROUND(RAND() * 11 + 1)) DAY) AS date,
       100
  FROM student
       CROSS JOIN subject ON name_student LIKE 'Востров С%'
 ORDER BY date;

SELECT * FROM student;

SELECT * FROM attempt;
