SELECT name_author
FROM author JOIN (
    SELECT author_id, COUNT(author_id) count_autor_id
    FROM (
        SELECT author_id, genre_id
        FROM book
        GROUP BY author_id, genre_id
         ) query_in
    GROUP BY author_id
                 ) query_in_2 USING(author_id)
WHERE count_autor_id = 1
ORDER BY name_author;

