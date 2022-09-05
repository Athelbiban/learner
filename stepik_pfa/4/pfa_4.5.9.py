"""
Магический квадрат 🌶️
Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n,
составленная из всех чисел 1, 2, 3, \ldots, n^21,2,3,…,n
2
  так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
  Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы
матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.

Sample Input 1:
3
8 1 6
3 5 7
4 9 2

Sample Output 1:
YES
"""


def sequence_elem(num, matrix):
    test = list(range(1, num * num + 1))
    original = sorted(sum(matrix, []))
    return True if original == test else False


def sum_row_col_diag(num, matrix):
    sum_main_diag = 0
    sum_side_diag = 0
    for i in range(num):
        sum_main_diag += matrix[i][i]
        sum_side_diag += matrix[i][~i]
    for e in range(num):
        sum_row = 0
        sum_col = 0
        for k in range(num):
            sum_row += matrix[e][k]
            sum_col += matrix[k][e]
        if not sum_row == sum_col == sum_main_diag == sum_side_diag:
            return False
    return True


def main():
    n = int(input())
    x = [[int(e) for e in input().split()] for _ in range(n)]
    if not sequence_elem(n, x) or not sum_row_col_diag(n, x):
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    print(main())
