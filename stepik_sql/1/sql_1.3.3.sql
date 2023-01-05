SELECT author Автор, COUNT(author) Различных_книг, SUM(amount) Количество_экземпляров
FROM book
GROUP BY author;

