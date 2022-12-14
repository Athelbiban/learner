"""
Книги на прочтение
Руслан получил в конце учебного года список литературы на лето. Теперь ему надо
выяснить, какие книги из этого списка у него есть. У Руслана на компьютере в
текстовом файле записаны все книги из его домашней библиотеки в случайном порядке.

Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.

Формат входных данных
На вход программе в первой строке подается натуральное число m — количество
книг в домашней библиотеке Руслана. Во второй строке записано натуральное
число n —  количество книг в списке на лето. Далее идут m строк с названиями
книг из домашней библиотеки и n строк названий из списка на лето.

Формат выходных данных
Программа должна вывести nn строк, в каждой из которых написано слово
YES, если книга найдена в библиотеке, и NO, если нет.

Sample Input:
4
4
Хоббит
Алиса в стране чудес
Том Сойер
Остров сокровищ
Буратино
Хоббит
Остров сокровищ
Война и мир

Sample Output:
NO
YES
YES
NO
"""


m, n = int(input()), int(input())
set1 = {input() for _ in range(m)}

for i in range(n):
    print('YES' if input() in set1 else 'NO')
