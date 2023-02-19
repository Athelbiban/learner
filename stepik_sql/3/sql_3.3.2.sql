SELECT name_enrollee
FROM program AS p
     JOIN program_enrollee AS pe ON p.program_id = pe.program_id
     AND name_program LIKE 'Мехатроника и робототехника'
     JOIN enrollee AS e ON pe.enrollee_id = e.enrollee_id
ORDER BY name_enrollee;
