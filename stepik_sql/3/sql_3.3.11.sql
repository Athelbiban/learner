SELECT DISTINCT name_program, name_enrollee
FROM program p
     JOIN program_enrollee pe ON p.program_id = pe.program_id
     JOIN enrollee e ON pe.enrollee_id = e.enrollee_id
     JOIN program_subject ps ON p.program_id = ps.program_id
     JOIN enrollee_subject es ON e.enrollee_id = es.enrollee_id
     AND ps.subject_id = es.subject_id
     AND result < min_result
ORDER BY name_program, name_enrollee;
