UPDATE fine f, payment p
   SET f.date_payment = p.date_payment,
       f.sum_fine = IF(DATEDIFF(p.date_payment, f.date_violation) <= 20, f.sum_fine / 2, f.sum_fine)
 WHERE (BINARY f.name,BINARY f.number_plate,BINARY f.violation, f.date_violation) =
       (p.name,p.number_plate,p.violation, p.date_violation)
   AND f.date_payment IS NULL;

SELECT * FROM fine;
