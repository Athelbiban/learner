a, b, c = [set(map(int, input().split())) for _ in '123']
d = set()

for i in a | b | c:
    if not (i in a and i in b and i in c):
        d.add(i)

print(*sorted(d))
