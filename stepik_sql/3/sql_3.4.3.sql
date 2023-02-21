DELETE FROM applicant
WHERE (program_id, enrollee_id) IN (
          SELECT DISTINCT pe.program_id, pe.enrollee_id
          FROM enrollee_subject AS es
                   JOIN program_subject AS ps ON es.subject_id = ps.subject_id
                   JOIN program_enrollee AS pe ON es.enrollee_id = pe.enrollee_id
                   AND pe.program_id = ps.program_id
                   AND result < min_result
          ORDER BY pe.program_id, pe.enrollee_id);

SELECT * FROM applicant
