"""
Old LCD calculator

Напишите программу, которая выводит число в стиле LCD калькулятора.

На вход программе подаётся последовательность цифр, которую нужно вывести на
экран в специальном стиле (см. пример).

Размер всех цифр 4 символа в ширину и 7 символов в высоту. Между цифрами
в выводе должен быть один пустой столбец. Перед первой цифрой не должно быть пробелов.

Выведенные цифры должны быть обведены рамочкой, в углах которой находится символ
x ("икс"), горизонтальная линия создаётся из символа - ("дефис"),
а вертикальная -- из символа вертикальной черты: |.

Формат ввода:
Строка произвольной длины (минимум один символ), содержащая последовательность цифр.

Формат вывода:
9 строк, содержащих цифры, записанные в указанном в задании формате.

Sample Input:
0123456789

Sample Output:
x-------------------------------------------------x
| --        --   --        --   --   --   --   -- |
||  |    |    |    | |  | |    |       | |  | |  ||
||  |    |    |    | |  | |    |       | |  | |  ||
|           --   --   --   --   --        --   -- |
||  |    | |       |    |    | |  |    | |  |    ||
||  |    | |       |    |    | |  |    | |  |    ||
| --        --   --        --   --        --   -- |
x-------------------------------------------------x
"""


num = input()
s0 = 'x' + '-' * len(num) * 4 + '-' * (len(num) - 1) + 'x'
start_end = '|'
s1 = [' -- ' for _ in range(len(num))]
s2 = ['|  |' for _ in range(len(num))]
s3 = ['|  |' for _ in range(len(num))]
s4 = [' -- ' for _ in range(len(num))]
s5 = ['|  |' for _ in range(len(num))]
s6 = ['|  |' for _ in range(len(num))]
s7 = [' -- ' for _ in range(len(num))]
n0 = [' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- ']
n1 = ['    ', '   |', '   |', '    ', '   |', '   |', '    ']
n2 = [' -- ', '   |', '   |', ' -- ', '|   ', '|   ', ' -- ']
n3 = [' -- ', '   |', '   |', ' -- ', '   |', '   |', ' -- ']
n4 = ['    ', '|  |', '|  |', ' -- ', '   |', '   |', '    ']
n5 = [' -- ', '|   ', '|   ', ' -- ', '   |', '   |', ' -- ']
n6 = [' -- ', '|   ', '|   ', ' -- ', '|  |', '|  |', ' -- ']
n7 = [' -- ', '   |', '   |', '    ', '   |', '   |', '    ']
n8 = [' -- ', '|  |', '|  |', ' -- ', '|  |', '|  |', ' -- ']
n9 = [' -- ', '|  |', '|  |', ' -- ', '   |', '   |', ' -- ']
d = {'0': n0, '1': n1, '2': n2, '3': n3, '4': n4, '5': n5, '6': n6, '7': n7, '8': n8, '9': n9}

for e, k in enumerate(num):
    s1[e] = d[k][0]
    s2[e] = d[k][1]
    s3[e] = d[k][2]
    s4[e] = d[k][3]
    s5[e] = d[k][4]
    s6[e] = d[k][5]
    s7[e] = d[k][6]

print(s0)
for i in s1, s2, s3, s4, s5, s6, s7:
    print(start_end, end='')
    print(*i, end='')
    print(start_end, end='')
    print()
print(s0)
