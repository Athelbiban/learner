"""
Задача «Уникальные элементы»
Условие
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том
порядке, в котором они встречаются в списке.
"""


s = [int(i) for i in input().split()]
count = 0
for i in range(len(s)):
    for e in range(len(s)):
        if s[i] == s[e]:
            count += 1
    if count == 1:
        print(s[i], end=' ')
    count = 0