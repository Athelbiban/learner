SELECT name_program
  FROM program
 WHERE name_program NOT IN (
            SELECT name_program
              FROM program AS p
                   JOIN program_subject AS ps ON p.program_id = ps.program_id
                   AND min_result < 40)
ORDER BY name_program;
