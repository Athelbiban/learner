n, m = map(int, input().split())
[print(*[str(i * n + j + 1).ljust(3) for i in range(m)]) for j in range(n)]
