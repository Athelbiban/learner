d = {}

for i in input().lower():
    if i not in '.,!?:;- ':
        d[i] = d.get(i, 0) + 1

for i in input().lower():
    if i not in '.,!?:;- ':
        d[i] = d.get(i, 0) - 1

print(('NO', 'YES')[min(d.values()) == max(d.values())])
