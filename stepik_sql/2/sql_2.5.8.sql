INSERT INTO buy_step (buy_id, step_id)
SELECT buy_id, step_id
FROM buy AS b, step AS s
WHERE b.buy_id = 5;

SELECT * FROM buy_step;
