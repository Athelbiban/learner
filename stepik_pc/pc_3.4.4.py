with open(r'files\dataset_3363_4.txt') as inf, open(r'files\answer.txt', 'w') as ouf:
    d, s = {}, [0, 0, 0]
    for line in inf:
        line = line.strip().split(';')
        ouf.write(f'{(int(line[1]) + int(line[2]) + int(line[3])) / 3}\n')
        d[line[0]] = d.get(line[0], [int(i) for i in line[1:]])
    for i in d.values():
        s[0] += i[0]
        s[1] += i[1]
        s[2] += i[2]
    ouf.write(f'{s[0] / len(d)} {s[1] / len(d)} {s[2] / len(d)}')
