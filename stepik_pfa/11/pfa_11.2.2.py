d = {}
for i in input().split():
    d[i] = d.get(i, 0) + 1
    print(d[i], end=' ')
