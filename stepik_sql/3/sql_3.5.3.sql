INSERT INTO step_keyword
SELECT step_id, keyword_id
FROM keyword k
     JOIN step s ON REGEXP_INSTR(step_name, CONCAT('\\b', keyword_name, '\\b'))
