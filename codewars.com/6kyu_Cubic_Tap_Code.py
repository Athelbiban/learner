def encode(string):
    s = ''
    for i in string:
        if i == ' ':
            s += '... ... ... '
        else:
            for k, l in enumerate(lst):
                for m, n in enumerate(lst[k]):
                    for j, h in enumerate(lst[k][m]):
                        if i not in n:
                            break
                        elif i == lst[k][m][j]:
                            s += '.' * (j + 1) + ' ' + '.' * (m + 1) + ' ' + '.' * (k + 1) + ' '
                            break
    return s.rstrip()


def decode(string):
    b = string.split()
    st = [[] for _ in range(len(b) // 3)]
    s = ''
    for i in range(len(b) // 3):
        c = 0
        for e in b:
            if c < 3:
                st[i] = [int(len(e) - 1)] + st[i]
                c += 1
            else:
                break
        del b[:3]
    for k, l, h in st:
        if lst[k][l][h] != '_':
            s += lst[k][l][h]
        else:
            s += ' '
    return s


lst = ((('A', 'B', 'C'),
        ('D', 'E', 'F'),
        ('G', 'H', 'I')),

       (('J', 'K', 'L'),
        ('M', 'N', 'O'),
        ('P', 'Q', 'R')),

       (('S', 'T', 'U'),
        ('V', 'W', 'X'),
        ('Y', 'Z', '_')))

print(encode('HELLO WORLD'))
print(decode(".. ... . .. .. . ... . .. ... . .. ... .. .. ... ... ... .. .. ... ... .. .. ... ... .. ... . .. . .. ."))
