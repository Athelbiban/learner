CREATE TABLE book (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    author_id INT NOT NULL,
    genre_id INT,
    price DECIMAL(8, 2),
    amount INT,
    FOREIGN KEY (author_id) REFERENCES author (author_id),
    FOREIGN KEY (genre_id) REFERENCES genre (genre_id)
);

DESCRIBE book;
