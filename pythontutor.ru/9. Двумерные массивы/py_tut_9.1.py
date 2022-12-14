"""
Задача «Максимум»
Условие
Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца,
в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько,
то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.

Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""


n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(n)]
max_i, max_j = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j - 1] < a[i][j] > a[max_i][max_j] or a[i - 1][j] < a[i][j] > a[max_i][max_j]:
            max_i, max_j = [i, j]
print(max_i, max_j)
