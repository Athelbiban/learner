"""
Заполнение спиралью 😈😈
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая
создает матрицу размером n×m заполнив её "спиралью" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

Sample Input 1:
4 5

Sample Output 1:
1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8
"""


n, m = map(int, input().split())
table = [[0] * m for _ in range(n)]
checklist = iter(list(range(1, n * m + 1)))
row, col, k = 0, 0, 0

while 0 in table[n // 2]:
    for i in range(k, m - k):
        col = i
        table[row][col] = str(next(checklist)).ljust(3)
    for i in range(k + 1, n - k):
        row = i
        table[row][col] = str(next(checklist)).ljust(3)
    if n > 1 and 0 in table[n // 2]:
        for i in range(m - 2 - k, -1 + k, -1):
            col = i
            table[row][col] = str(next(checklist)).ljust(3)
    if m > 1 and 0 in table[n // 2]:
        for i in range(n - 2 - k, 0 + k, -1):
            row = i
            table[row][col] = str(next(checklist)).ljust(3)
    k += 1

for i in table:
    print(*i)
