SELECT name_subject,
       COUNT(student_id) AS Количество,
       ROUND(AVG(result), 2) AS Среднее
FROM subject AS s
     LEFT JOIN attempt AS a USING(subject_id)
GROUP BY name_subject
ORDER BY Среднее DESC;
