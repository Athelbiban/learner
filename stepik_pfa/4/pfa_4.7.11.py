n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
c = [[0] * n for _ in range(n)]

for e in range(m - 1):
    for i in range(n):
        for j in range(n):
            for p in range(n):
                c[i][j] += x[i][p] * x[p][j]
        # print(*c[i])

for row in c:
    print(*row)
