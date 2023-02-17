INSERT INTO testing (attempt_id, question_id)
SELECT attempt_id, question_id
  FROM attempt AS a
       JOIN question AS q
       ON a.subject_id = q.subject_id
       AND attempt_id = (SELECT MAX(attempt_id) FROM attempt)
 ORDER BY RAND()
 LIMIT 3;

SELECT * FROM testing;
