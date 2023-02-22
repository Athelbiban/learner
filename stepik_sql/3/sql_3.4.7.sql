SET @temp1 := 0;
SET @temp2 := 1;

UPDATE applicant_order
SET str_id = IF(@temp2 = program_id, @temp1 := @temp1 + 1, @temp1 := 1 AND @temp2 := program_id);

SELECT * FROM applicant_order;
