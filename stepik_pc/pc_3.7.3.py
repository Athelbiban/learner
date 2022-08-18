lst1, lst2, s = [], [], set()
for _ in range(int(input())):
    lst1.append(input().lower())

for _ in range(int(input())):
    lst2 += [i.lower() for i in input().split()]

for i in lst2:
    if i not in lst1:
        s.add(i)

print(*s, sep='\n')
