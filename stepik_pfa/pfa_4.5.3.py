n, m = int(input()), int(input())
x = [[e for e in input().split()] for _ in range(n)]
a, b = [int(u) for u in input().split()]

for i in range(n):
    x[i][a], x[i][b] = x[i][b], x[i][a]
    print(*x[i])
