with open(r'files\test_doc.txt') as inf, open(r'files\answer.txt', 'w') as ouf:
    s, c = [0, 0, 0], 0
    for line in inf:
        line = line.strip().split(';')
        ouf.write(f'{(int(line[1]) + int(line[2]) + int(line[3])) / 3}\n')
        s[0] += int(line[1])
        s[1] += int(line[2])
        s[2] += int(line[3])
        c += 1
    ouf.write(f'{s[0] / c} {s[1] / c} {s[2] / c}')
