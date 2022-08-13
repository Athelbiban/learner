with open(r'files\dataset_3363_3.txt') as file:
    s, d = [], {}
    for i in file:
        s += i.strip().lower().split()
    for i in s:
        d[i] = d.get(i, 0) + 1

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    m = 0

    for i, e in enumerate(d):
        if e[1] < m:
            del d[i:]
        else:
            m = e[1]
    d = sorted(d, key=lambda x: x[0])

with open(r'files\answer.txt', 'w') as file:
    file.write(f'{d[0][0]} {d[0][1]}')
