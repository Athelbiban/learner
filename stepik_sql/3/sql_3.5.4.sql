SELECT CONCAT(m.module_id, '.',
                 l.lesson_position, '.',
                    IF(step_position < 10, CONCAT('0', step_position), step_position), ' ',
                        step_name) Шаг
FROM step s
     JOIN lesson l ON s.lesson_id = l.lesson_id
     JOIN module m ON l.module_id = m.module_id
     JOIN step_keyword sk ON s.step_id = sk.step_id
     JOIN keyword k ON sk.keyword_id = k.keyword_id
WHERE keyword_name = 'AVG' OR keyword_name = 'MAX'
GROUP BY s.step_id
HAVING COUNT(s.step_id) = 2
ORDER BY Шаг;
