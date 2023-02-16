SELECT question_id, name_question
  FROM question AS q
       JOIN subject AS s
       ON q.subject_id = s.subject_id
       AND name_subject = 'Основы баз данных'
 ORDER BY RAND()
 LIMIT 3;
