  SELECT name, number_plate, violation
    FROM fine
GROUP BY name, number_plate, violation
  HAVING COUNT(name) > 1
ORDER BY name, number_plate, violation;
