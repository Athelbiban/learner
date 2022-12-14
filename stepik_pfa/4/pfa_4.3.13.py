"""
Разбиение на чанки 🌶️
На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска),
а возвращает список из чанков указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела
и число nn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Sample Input 1:
a b c d e f
2

Sample Output 1:
[['a', 'b'], ['c', 'd'], ['e', 'f']]
"""


def chunked(lst, n):
    # Мой return:
    # return [lst[n*i:n*i+n] for i in range(-1 * len(lst) // n * -1)]
    # return здорового человека:
    return [lst[i:i+n] for i in range(0, len(lst), n)]


if __name__ == '__main__':
    print(chunked(input().split(), int(input())))
