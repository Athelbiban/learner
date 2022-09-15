n = int(input())
s = set(map(int, input()))

for _ in range(n - 1):
    s.intersection_update(map(int, input()))

print(*sorted(s))
