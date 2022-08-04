lst = sorted(input().split())
s = set()
temp = []
for i in lst:
    if i not in temp:
        temp.append(i)
    else:
        s.add(i)
print(*s)
