"""
Задача «Проценты»
Условие
Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
Вклад составляет X рублей Y копеек. Определите размер вклада через год.
Программа получает на вход целые числа P, X, Y и должна вывести два числа: величину вклада
через год в рублях и копейках. Дробная часть копеек отбрасывается.
"""


p, x, y = int(input()), int(input()), int(input())

print(int((x + x * p / 100) // 1 + ((y + y * p / 100) // 100)) /
      + int(((y + y * p / 100) % 100 + round((x + x * p / 100) % 1, 2) * 100)) // 100)
print(int(((y + y * p / 100) % 100 + round((x + x * p / 100) % 1, 2) * 100) % 100))
