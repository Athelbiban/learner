SELECT name_question, name_answer, IF(is_correct, 'Верно', 'Неверно') AS Результат
FROM question AS q
     JOIN testing AS t USING(question_id)
     JOIN answer AS a USING(answer_id)
WHERE attempt_id = 7
