n = int(input())
x = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == n + ~j:
            x[i][j] = 1
        elif i > n + ~j:
            x[i][j] = 2
    print(*x[i])
