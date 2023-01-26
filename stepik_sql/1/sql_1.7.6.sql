/*
SELECT fine_id, name, number_plate, violation,
       IF(name IN (
              SELECT name
                FROM fine
            GROUP BY name, number_plate, violation
              HAVING COUNT(name) > 1
                   ) AND date_payment IS NULL, sum_fine * 2, sum_fine),
       date_violation, date_payment
  FROM fine;
*/

UPDATE fine f, (
        SELECT name, number_plate, violation
          FROM fine
      GROUP BY name, number_plate, violation
        HAVING COUNT(name) > 1
               ) q
   SET sum_fine = sum_fine * 2
 WHERE f.name = q.name
   AND f.number_plate = q.number_plate
   AND f.violation = q.violation
   AND f.date_payment IS NULL;

SELECT * FROM fine;
