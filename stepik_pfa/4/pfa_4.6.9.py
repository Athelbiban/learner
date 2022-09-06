n, m = map(int, input().split())
x = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == m - j - 1 + 0:
            x[i][j] = i * m + j + 1
    print(*x[i])
