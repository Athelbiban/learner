"""
Задача «Стоимость покупки»
Условие
Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей
и копеек нужно заплатить за n пирожков. Программа получает на вход три
числа: a, b, n, и должна вывести два числа: стоимость покупки в рублях и копейках.
"""


a, b, n = int(input()), int(input()), int(input())

x = n * a + (n * b) // 100
y = (n * b) % 100

print(x, y)
