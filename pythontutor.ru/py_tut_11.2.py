"""
Задача «Словарь синонимов»
Условие
Вам дан словарь, состоящий из пар слов. Каждое слово является
синонимом к парному ему слову. Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.
"""


d1, d2 = dict(), dict()
for i in range(int(input())):
    a, b = input().split()
    d1[a] = b
    d2[b] = a
s = input()
print(d1.get(s, ''), d2.get(s, ''), sep='')
