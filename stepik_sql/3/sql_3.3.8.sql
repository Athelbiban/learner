SELECT name_department, name_program, plan,
       COUNT(enrollee_id) AS Количество,
       ROUND(COUNT(enrollee_id) / plan, 2) AS Конкурс
FROM program AS p
     LEFT JOIN program_enrollee AS pe ON p.program_id = pe.program_id
     JOIN department AS d ON p.department_id = d.department_id
GROUP BY name_department, name_program, plan
ORDER BY Конкурс DESC;
