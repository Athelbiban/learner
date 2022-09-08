n, m = map(int, input().split())
a = [[int(j) for j in input().split()] for _ in range(n)]
input()
b = [[int(j) for j in input().split()] for _ in range(n)]
[print(*[a[i][j] + b[i][j] for j in range(m)]) for i in range(n)]
