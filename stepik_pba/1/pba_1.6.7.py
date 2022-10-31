"""
12
A
X
B : A
C : A
Y : A X
Z : X
D : B C
V : Y Z
E : D
F : D
W : V
G : F
"""


def class_inheritance(ancestor, descendant):
    global d

    def func(u):
        if u == ancestor:
            return True
        return class_inheritance(ancestor, u)

    if descendant == 'object':
        return False
    for k in d[descendant]:
        func(k)
    return False


d = {}

for n in range(int(input())):
    lst = input().split()
    if len(lst) > 1:
        del lst[1]
        d[lst[0]] = d.get(lst[0], []) + lst[1:]
    else:
        d[lst[0]] = d.get(lst[0], ['object'])

for q in range(int(input())):
    a, b = input().split()
    print(('No', 'Yes')[class_inheritance(a, b)])
