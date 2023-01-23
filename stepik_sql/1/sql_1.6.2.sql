SELECT name, city, per_diem, date_first, date_last
FROM trip
WHERE name LIKE '%а %'
ORDER BY date_last DESC;

--Решение через SUBSTRING_INDEX
/*
select name, city, per_diem, date_first, date_last from trip
WHERE RIGHT(SUBSTRING_INDEX(name,' ',1),1) = 'а' 
order by date_last DESC
*/
