n = int(input())
x = [[e for e in input().split()] for _ in range(n)]

for i in range(n // 2):
    x[i], x[~i] = x[~i], x[i]

for row in x:
    print(*row)
