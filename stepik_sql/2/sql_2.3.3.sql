INSERT INTO author (name_author)
SELECT author
FROM supply
WHERE author NOT IN (SELECT name_author FROM author);

SELECT * FROM author;
