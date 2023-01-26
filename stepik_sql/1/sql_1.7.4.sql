UPDATE fine f, traffic_violation tv
   SET f.sum_fine = tv.sum_fine
 WHERE f.violation COLLATE utf8mb4_unicode_ci = tv.violation
   AND f.sum_fine IS NULL;

SELECT * FROM fine;
