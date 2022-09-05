"""
Заполнение 5 🌶️
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая
создает матрицу размером n \times mn×m заполнив её в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm —
количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33
символа на каждый элемент. Для этого используйте строковый метод ljust().
Можно обойтись и без ljust(), система примет и такое решение 😇

Sample Input 1:
5 5

Sample Output 1:
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4
"""


n, m = map(int, input().split())    # Вариант 1
x = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        x[i][j] = str((i + j) % m + 1).ljust(3)
    print(*x[i])


# n, m = map(int, input().split())    # Вариант 2
# [print(*[str((i + j) % m + 1).ljust(3) for j in range(m)]) for i in range(n)]
