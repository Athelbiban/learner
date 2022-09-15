s = set()

for i in map(int, input().split()):
    print(('NO', 'YES')[i in s])
    s.add(i)
