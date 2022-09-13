"""
Книги на прочтение 🌶️
Ученики 1010 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:

"Что такое математика?";
"Математическая составляющая";
"100 гениальных идей по математике".

Оказалось, что n учеников прочитали первую книгу, m учеников — вторую, k учеников — третью.
Также известно, что x учеников прочли первую или вторую, или обе эти книги, y учеников — вторую
или третью, или обе, zz учеников — первую и третью, или хотя бы одну из этих двух книг.
Полностью выполнили задание только tt учеников. Всего в 1010 классе учится aa учеников. Напишите
программу, которая выводит сколько учеников:

прочитали только одну книгу;
прочитали две книги;
не прочитали ни одной из рекомендованных книг.

Формат входных данных
На вход программе подаются числа n, m, k, x, y, z, t, a каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа в соответствии с условием задачи, каждое на отдельной строке.

Sample Input:
19
18
22
32
33
35
2
50

Sample Output:
29
12
7
"""


n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
print(2*x + 2*y + 2*z - 3*n - 3*k - 3*m + 3*t)
print(2*n + 2*k + 2*m - x - y - z - 3*t)
print(a-x-y-z+n+k+m-t)
