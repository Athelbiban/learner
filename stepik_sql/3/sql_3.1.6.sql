SELECT name_subject, COUNT(DISTINCT(student_id)) AS Количество
FROM subject AS s
    LEFT JOIN attempt AS a USING(subject_id)
GROUP BY name_subject
ORDER BY Количество DESC, name_subject;
