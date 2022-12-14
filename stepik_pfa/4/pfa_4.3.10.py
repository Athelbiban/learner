"""
Треугольник Паскаля 1 🌶️
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму.
В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....

На вход программе подается число nn. Напишите программу, которая возвращает указанную строку
треугольника Паскаля в виде списка (нумерация строк начинается с нуля).

Формат входных данных
На вход программе подается число n (n≥0).

Формат выходных данных
Программа должна вывести указанную строку треугольника Паскаля в виде списка.

Примечание 1. Решение удобно оформить в виде функции pascal(), которая принимает номер
строки и возвращает соответствующую строку треугольника Паскаля.
"""


def pascal(n):
    c = [1]
    for k in range(1, n // 2 + 1):
        c.append(c[k - 1] * (n - k + 1) // k)
    return c + c[::-1] if n % 2 else c + c[-2::-1]


if __name__ == '__main__':
    print(pascal(int(input())))
