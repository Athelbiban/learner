def class_inheritance(parent, child, path=[]):
    path = path + [child]
    if child == parent:
        return path
    if not d[child]:
        return False
    for par in d[child]:
        if par not in path:
            newpath = class_inheritance(parent, par, path)
            if newpath:
                return True
    return False


d = {}
for _ in range(int(input())):
    s = input().split()
    d[s[0]] = d.get(s[0], []) + s[2:]

lst = []
for _ in range(int(input())):
    a, b = input().split()
    flag = True
    if a != b:
        flag = class_inheritance(a, b)
    lst.append(flag)
[print(('No', 'Yes')[f]) for f in lst]
