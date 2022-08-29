"""
Последовательность треугольных чисел образуется путем сложения натуральных чисел. К примеру,
7-е треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Перечислим делители первых семи треугольных чисел:

 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

Каково первое треугольное число, у которого более пятисот делителей?
"""


import time

start = time.time()


def prime_dividers(n, lst, e=2):
    if n == 1:
        return lst
    else:
        for i in range(e, n + 1):
            if n % i == 0:
                lst.append(i)
                return prime_dividers(n // i, lst, i)


def all_dividers(s):
    div = 1
    a = s[0]
    counter = 1
    for i in s:
        if i == a:
            counter += 1
        else:
            div *= counter
            counter = 2
            a = i
    return div * counter


def main():
    numb = 2
    while True:
        lst = []
        triangle_numb = (numb * (numb + 1)) // 2
        prime_div = prime_dividers(triangle_numb, lst)
        all_div = all_dividers(prime_div)
        if all_div < 500:
            numb += 1
        else:
            break
    return f'Номер треугольного числа: {numb}\n' \
           f'Треугольное число: {triangle_numb}\n' \
           f'Количество делителей: {all_div}'


if __name__ == '__main__':
    print(main())


end = time.time() - start
print(f'Время выполнения (сек.): {end}')
