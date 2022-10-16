import math


def higher_order_function(key, n):
    def func(degree):
        return n ** degree
    d = {'квадрат': func(2), 'куб': func(3), 'корень': math.sqrt(n), 'модуль': abs(n), 'синус': math.sin(n)}
    return d[key]


num = int(input())
print(higher_order_function(input(), num))
