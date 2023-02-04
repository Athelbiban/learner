UPDATE book
SET genre_id = (
    SELECT genre_id
    FROM genre
    WHERE name_genre = 'Поэзия'
    )
WHERE title = 'Стихотворения и поэмы'
  AND author_id = (
      SELECT author_id
      FROM author
      WHERE name_author = 'Лермонтов М.Ю.'
    );

UPDATE book
SET genre_id = (
    SELECT genre_id
    FROM genre
    WHERE name_genre = 'Приключения'
    )
WHERE title = 'Остров сокровищ'
  AND author_id = (
      SELECT author_id
      FROM author
      WHERE name_author = 'Стивенсон Р.Л.'
    );

SELECT * FROM book;
