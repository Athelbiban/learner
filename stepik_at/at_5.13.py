d = {}

for i in input().split():
    d[len(i)] = d.get(len(i), 0) + 1

print(*[f'{k}: {v}' for k, v in sorted(d.items())], sep='\n')
