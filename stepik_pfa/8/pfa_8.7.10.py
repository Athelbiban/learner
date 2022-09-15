a, b, c = [set(map(int, input().split())) for _ in '...']

print(*sorted(a & b - c, reverse=True))
