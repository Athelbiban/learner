"""
Диагонали параллельные главной
На вход программе подается натуральное число n. Напишите программу, которая
создает матрицу размером n×n и заполняет её по следующему правилу:

на главной диагонали на месте каждого элемента должно стоять число 00;
на двух диагоналях, прилегающих к главной, число 11;
на следующих двух диагоналях число 22, и т.д.
Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

Sample Input 1:
5

Sample Output 1:
0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0
"""


n = int(input())
x = [[0] * n for _ in range(n)]

for e in range(1, n):
    for i in range(n):
        for j in range(n):
            if i == j + e or i == j - e:
                x[i][j] = e

for row in x:
    print(*row)