a, b, c = [set(input().split()) for _ in '...']

print(*sorted(c - (a | b), key=int, reverse=True))
