n, m = map(int, input().split())
x = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2:
            x[i][j] = '*'
    print(*x[i])
