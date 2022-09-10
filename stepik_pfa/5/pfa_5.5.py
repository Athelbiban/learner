"""
Симметричная матрица
Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.

Sample Input 1:
3
0 3 10
4 9 3
7 4 0

Sample Output 1:
YES
"""


n = int(input())
x = [[k for k in input().split()] for _ in range(n)]
flag = 'YES'

for e in range(1, n):
    t = []
    y = []
    for i in range(n):
        for j in range(n):
            if i == n + ~j - e:
                t.append(x[i][j])
            elif i == n + ~j + e:
                y.append(x[i][j])
    if y != t:
        flag = 'NO'
        break

print(flag)
