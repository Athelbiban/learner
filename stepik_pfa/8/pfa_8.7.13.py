a, b, c = [set(map(int, input().split())) for _ in '123']
d = set(range(11))
print(*sorted(d - a - b - c))
