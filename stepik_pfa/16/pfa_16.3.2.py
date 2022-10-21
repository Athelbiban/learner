"""
Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce().

def product_of_odds(data):   # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result
Примечание 1. Тестирующая система никак не "покарает" вас за неиспользование встроенных функций
filter() и reduce(), однако лучше сделать это задание честно 😃.
"""


from functools import reduce


def product_of_odds(data):
    return reduce(lambda x, y: x*y, filter(lambda i: i % 2, data), 1)


print(product_of_odds([1, 2, 3, 4, 5, 6]))
