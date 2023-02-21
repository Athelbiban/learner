UPDATE applicant a
       JOIN (SELECT enrollee_id, SUM(bonus) sum_bonus
             FROM achievement ac
                  JOIN enrollee_achievement ea ON ac.achievement_id = ea.achievement_id
             GROUP BY enrollee_id
             ) ac ON a.enrollee_id = ac.enrollee_id
SET itog = itog + sum_bonus;

SELECT * FROM applicant;
