"""
Задача «Продажи»
Условие
Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой
запись вида Покупатель товар количество, где Покупатель — имя покупателя (строка без пробелов), товар —
название товара (строка без пробелов), количество — количество приобретенных единиц товара.

Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц
каждого вида товаров. Список покупателей, а также список товаров для каждого покупателя нужно выводить в
лексикографическом порядке.
"""


def inputs():
    while True:
        try:
            string = input().split()
            yield string
        except (ValueError, EOFError):
            string_sort = sorted(d.items())
            for i in range(len(string_sort)):
                print(string_sort[i][0] + ':')
                for purchase, count in sorted(string_sort[i][1].items()):
                    print(purchase, count)
            return

d = {}

for name, purchase, count in inputs():
    d.setdefault(name, {})
    d[name][purchase] = d[name].get(purchase, 0) + int(count)
