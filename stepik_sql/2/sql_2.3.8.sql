DELETE FROM a
USING author a JOIN book b USING(author_id) JOIN genre g USING(genre_id)
WHERE name_genre = 'Поэзия';

SELECT * FROM author;

SELECT * FROM book;
