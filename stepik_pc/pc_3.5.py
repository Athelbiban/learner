def f(a):
    return a


d = {}

for i in range(int(input())):
    x = int(input())
    d[x] = d.get(x, 0)
    if not d[x]:
        d[x] = f(x)
    print(d[x])
