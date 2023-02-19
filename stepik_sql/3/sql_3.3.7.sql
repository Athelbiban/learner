SELECT name_enrollee, SUM(IFNULL(bonus, 0)) AS Бонус
FROM achievement AS a
     JOIN enrollee_achievement AS ea ON a.achievement_id = ea.achievement_id
     RIGHT JOIN enrollee AS e ON ea.enrollee_id = e.enrollee_id
GROUP BY name_enrollee
ORDER BY name_enrollee;
