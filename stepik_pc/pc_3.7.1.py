d = {}

for _ in range(int(input())):
    n = input().split(';')
    d[n[0]] = d.get(n[0], [0, 0, 0, 0, 0])
    d[n[2]] = d.get(n[2], [0, 0, 0, 0, 0])
    d[n[0]][0] += 1
    d[n[2]][0] += 1
    if int(n[1]) > int(n[3]):
        d[n[0]][1] += 1
        d[n[0]][4] += 3
        d[n[2]][3] += 1
    elif int(n[1]) < int(n[3]):
        d[n[2]][1] += 1
        d[n[2]][4] += 3
        d[n[0]][3] += 1
    else:
        d[n[0]][2] += 1
        d[n[0]][4] += 1
        d[n[2]][2] += 1
        d[n[2]][4] += 1

for k, v in d.items():
    print(f'{k}:{v[0]} {v[1]} {v[2]} {v[3]} {v[4]}')
