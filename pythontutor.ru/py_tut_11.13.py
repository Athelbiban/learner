"""
Задача «Родословная: LCA»
Условие
В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor).
Наименьшим общим предком элементов A и B является такой элемент C, что С является предком A, C является предком
B, при этом глубина C является наибольшей из возможных. При этом элемент считается своим собственным предком.

Формат входных данных аналогичен предыдущей задаче

Для каждого запроса выведите наименьшего общего предка данных элементов.
"""


def line_tree1(human):
    c.append(human)
    if human not in d.keys():
        return human
    else:
        return line_tree1(d[human])


def line_tree2(human):
    b.append(human)
    if human not in d.keys():
        return human
    else:
        return line_tree2(d[human])


d = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    d[child] = d.get(child, parent)

k = int(input())
for i in range(k):
    c = []
    b = []
    first, second = input().split()
    line_tree1(first)
    line_tree2(second)
    f = []
    for e in c:
        for u in b:
            if e == u:
                f.append(e)
    print(f[0])
