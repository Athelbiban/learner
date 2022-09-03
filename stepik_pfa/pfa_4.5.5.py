n = int(input())
x = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    x[i][i], x[~i][i] = x[~i][i], x[i][i]

for i in x:
    print(*i)
