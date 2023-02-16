CREATE TABLE IF NOT EXISTS new_table
SELECT name_subject,
       CONCAT(LEFT(name_question, 30), '...') AS Вопрос,
       ROUND(AVG(is_correct) * 100, 2) AS U
  FROM subject AS su
       JOIN question AS q USING(subject_id)
       JOIN testing AS t USING(question_id)
       JOIN answer AS a ON t.answer_id = a.answer_id
 GROUP BY name_subject, name_question;

SELECT name_subject, Вопрос, 'Самый сложный' AS Сложность
  FROM new_table
 WHERE U = (SELECT MIN(U) FROM new_table)
 UNION ALL
SELECT name_subject, Вопрос, 'Самый легкий' AS Сложность
  FROM new_table
 WHERE U = (SELECT MAX(U) FROM new_table);

DROP TABLE IF EXISTS new_table;
