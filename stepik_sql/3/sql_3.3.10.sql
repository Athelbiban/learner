SELECT name_program, name_enrollee, SUM(result) AS itog
  FROM enrollee AS e
       JOIN enrollee_subject AS es ON e.enrollee_id = es.enrollee_id
       JOIN program_subject AS ps ON es.subject_id = ps.subject_id
       JOIN program AS p ON ps.program_id = p.program_id
       JOIN program_enrollee AS pe ON e.enrollee_id = pe.enrollee_id
       AND pe.program_id = p.program_id
 GROUP BY name_program, name_enrollee
 ORDER BY name_program, itog DESC;
