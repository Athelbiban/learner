CREATE TABLE applicant
SELECT pe.program_id, es.enrollee_id, SUM(result) AS itog
FROM enrollee_subject AS es
         JOIN program_subject AS ps ON es.subject_id = ps.subject_id
         JOIN program_enrollee AS pe ON es.enrollee_id = pe.enrollee_id
         AND pe.program_id = pe.program_id
GROUP BY pe.program_id, es.enrollee_id
ORDER BY pe.program_id, itog DESC;
