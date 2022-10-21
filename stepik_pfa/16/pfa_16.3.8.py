"""
Напишите функцию arithmetic_operation(), которая принимает символ одной из
четырех арифметических операций (+, -, *, /) и возвращает функцию двух
аргументов для соответствующей операции.

Примечание 1. Приведенный ниже код, при условии, что функция arithmetic_operation() написана правильно

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
должен выводить:

30
4.0
"""


from operator import add as a, sub as s, mul as m, truediv as t


def arithmetic_operation(operation):
    return (a, s, m, t)[['+', '-', '*', '/'].index(operation)]


add = arithmetic_operation('+')
div = arithmetic_operation('/')
mul = arithmetic_operation('*')
print(add(10, 20))
print(div(20, 5))
print(mul(2, 3))
