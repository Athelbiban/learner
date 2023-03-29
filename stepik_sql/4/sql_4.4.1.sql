WITH cte AS (
    SELECT name_subject, name_question, AVG(is_correct) AS avg_test
    FROM subject
         JOIN question USING(subject_id)
         JOIN testing USING(question_id)
         JOIN answer USING(answer_id)
    GROUP BY name_subject, name_question)

SELECT name_subject, name_question,
       CASE
           WHEN avg_test = (SELECT MAX(avg_test) FROM cte) THEN 'самый легкий'
           WHEN avg_test = (SELECT MIN(avg_test) FROM cte) THEN 'самый сложный'
       END AS Сложность
FROM cte
HAVING Сложность IS NOT NULL
ORDER BY avg_test DESC;
