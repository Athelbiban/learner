CREATE TABLE applicant_order
SELECT *
FROM applicant
ORDER BY program_id, itog DESC;

DROP TABLE applicant;
