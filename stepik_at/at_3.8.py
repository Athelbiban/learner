"""
Выведите таблицу размером n×n, заполненную целыми числами от 11 до n^2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере.

Формат ввода:
Одна строка, содержащая одно целое число n, n > 0.

Формат вывода:
Таблица из n строк, значения в строках разделены пробелом.

Sample Input:
5

Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

P.S. Задача аналогична pc_2.6.11 (Stepik курс для новичков от Bioinformatics Institute)
и похожа на задачу pfa_4.6.10 (Stepik курс для продвинутых от BeeGeek).
"""


n = int(input())
table = [[0] * n for _ in range(n)]
checklist = iter(list(range(1, n * n + 1)))
row, col, k = 0, 0, 0

while not table[n // 2][(n - 1) // 2]:
    for i in range(k, n - k):
        col = i
        table[row][col] = str(next(checklist)).ljust(3)
    for i in range(k + 1, n - k):
        row = i
        table[row][col] = str(next(checklist)).ljust(3)
    for i in range(n - 2 - k, -1 + k, -1):
        col = i
        table[row][col] = str(next(checklist)).ljust(3)
    for i in range(n - 2 - k, 0 + k, -1):
        row = i
        table[row][col] = str(next(checklist)).ljust(3)
    k += 1

for i in table:
    print(*i)
