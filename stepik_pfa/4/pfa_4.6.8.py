n, m = map(int, input().split())
y = iter(range(1, n * m + 1))
x = [[] for _ in range(n)]

for i in range(n):
    for _ in range(m):
        if i % 2:
            x[i].insert(0, str(next(y)).ljust(3))
        else:
            x[i].append(str(next(y)).ljust(3))
    print(*x[i])
