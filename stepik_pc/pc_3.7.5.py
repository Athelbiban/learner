with open(r'files/dataset_3380_5.txt', encoding='utf-8') as inf,\
        open(r'files/answer.txt', 'w', encoding='utf-8') as ouf:
    d, s = {str(i): '-' for i in range(1, 12)}, []
    for i in inf:
        c, _, h = i.split()
        h, s = int(h), s + [c]
        d[c] = h if d[c] == '-' else d[c] + h
    for k, v in d.items():
        ouf.write(f'{k} {v / s.count(k) if v != "-" else v}\n')
