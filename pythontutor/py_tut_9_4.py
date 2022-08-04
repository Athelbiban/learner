n = int(input())
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(abs(j - i))
for row in a:
    print(' '.join(map(str, row)))
