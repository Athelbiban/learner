e = set()

for _ in range(int(input())):
    e |= set(input().lower())

print(len(e))
