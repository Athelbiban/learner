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


def class_inheritance(end, start, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not d[start]:
        return False
    for anc in d[start]:
        if anc not in path:
            newpath = class_inheritance(end, anc, path)
            if newpath:
                return True
    return False


d = {}

for n in range(int(input())):
    lst = input().split()
    if len(lst) > 1:
        del lst[1]
        d[lst[0]] = d.get(lst[0], []) + lst[1:]
    else:
        d[lst[0]] = d.get(lst[0], [])

for q in range(int(input())):
    a, b = input().split()
    c = True
    if a != b:
        c = class_inheritance(a, b)
    print(('No', 'Yes')[c])
