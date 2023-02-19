SELECT name_program, plan
FROM program
WHERE plan IN (SELECT MAX(plan) FROM program)
