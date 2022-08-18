with open(r'files\dataset_3363_3(1).txt') as inf, open(r'files\answer.txt', 'w') as ouf:
    d = {}
    s = sorted(inf.read().strip().lower().split())
    for i in s:
        d[i] = d.get(i, 0) + 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    ouf.write(f'{d[0][0]} {d[0][1]}')
