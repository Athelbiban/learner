n = input().split()

for i in range(1, len(n), 2):
    n[i], n[i-1] = n[i-1], n[i]

print(*n)
