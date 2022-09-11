t = [input().split() for _ in range(int(input()))]
[print(*e) for e in t]
print()
[print(*i) for i in t if i[1] >= '4']
