SELECT name_program
FROM subject AS s
     JOIN program_subject AS ps ON s.subject_id = ps.subject_id
     AND name_subject = 'Информатика'
     JOIN program AS p ON ps.program_id = p.program_id
ORDER BY name_program DESC;
