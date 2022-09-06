def encode(string):
    s = ''
    for i in string:
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
    st = [[b[i + 2], b[i + 1], b[i]] for i in range(0, len(b), 3)]
    s = ''
    for i in st:
        s += lst[len(i[0]) - 1][len(i[1]) - 1][len(i[2]) - 1]
    return s


lst = ((('A', 'B', 'C'),
        ('D', 'E', 'F'),
        ('G', 'H', 'I')),

       (('J', 'K', 'L'),
        ('M', 'N', 'O'),
        ('P', 'Q', 'R')),

       (('S', 'T', 'U'),
        ('V', 'W', 'X'),
        ('Y', 'Z', ' ')))

print(encode('HELLO WORLD'))
print(decode(".. ... . .. .. . ... . .. ... . .. ... .. .. ... ... ... .. .. ... ... .. .. ... ... .. ... . .. . .. ."))
