SELECT q.name_program
  FROM (
       SELECT name_program, name_subject
         FROM subject AS s
              JOIN program_subject AS ps
              ON s.subject_id = ps.subject_id
              AND name_subject = 'Математика'
              JOIN program AS p ON ps.program_id = p.program_id) AS q
       JOIN (
            SELECT name_program, name_subject
              FROM subject AS s
                   JOIN program_subject AS ps
                   ON s.subject_id = ps.subject_id
                   AND name_subject = 'Информатика'
                   JOIN program AS p
                   ON ps.program_id = p.program_id) AS q2
       ON q.name_program = q2.name_program
 ORDER BY name_program;
