"""
Задача «Переставить min и max»
Условие
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""


s = [int(i) for i in input().split()]
i_max = s.index(max(s))
i_min = s.index(min(s))
s[i_max], s[i_min]= s[i_min], s[i_max]
print(' '.join([str(i) for i in s]), end='')
