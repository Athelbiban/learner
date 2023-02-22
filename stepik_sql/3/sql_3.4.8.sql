CREATE TABLE student
SELECT name_program, name_enrollee, itog
FROM program p
     JOIN applicant_order ao on p.program_id = ao.program_id
     AND ao.str_id <= p.plan
     JOIN enrollee e ON e.enrollee_id = ao.enrollee_id
ORDER BY name_program, itog DESC;

SELECT * FROM student;
