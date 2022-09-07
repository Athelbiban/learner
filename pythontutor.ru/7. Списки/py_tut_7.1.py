"""
Задача «Четные индексы»
Условие
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""


list_A = [i for i in input().split()]
for i in range(len(list_A)):
    if i % 2 == 0:
        print(list_A[i], end=' ')
