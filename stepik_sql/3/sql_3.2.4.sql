UPDATE attempt
   SET result = (SELECT ROUND(AVG(IFNULL(is_correct, 0)) * 100)
                   FROM answer AS a
                        RIGHT OUTER JOIN testing AS t ON a.answer_id = t.answer_id
                  WHERE attempt_id = 8)
 WHERE attempt_id = 8;

SELECT * FROM attempt;
