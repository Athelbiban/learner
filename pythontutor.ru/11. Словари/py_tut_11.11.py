"""
Задача «Родословная: подсчет уровней»
Условие
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.

Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника
высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.

Вам дано генеалогическое древо, определите высоту всех его элементов.

Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие
родителя для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени
каждого элемента необходимо вывести его высоту.

Примечание
Эта задача имеет решение сложности O(n), но вам достаточно написать решение сложности O(n2) (не считая сложности
обращения к элементам словаря).
"""

from collections import defaultdict


def elem_of_tree():
    b = c.copy()
    for i in b:
        for e in d[i]:
            c[e] = c.get(e, c[i] + 1)
    if len(s) == len(c):
        for n in sorted(c):
            print(n, c[n])
    else:
        return elem_of_tree()


def progenitor():
    z = {}
    for i in d.keys():
        for e in d.keys():
            if i in d[e]:
                z[i] = z.get(i)
    progenitor = tuple(set(d.keys()) - set(z))[0]
    c[progenitor] = 0


d = defaultdict(list)
c = {}
s = set()

for i in range(int(input()) - 1):
    child, parent = input().split()
    d[parent].append(child)
    s.add(parent)
    s.add(child)

progenitor()
elem_of_tree()
