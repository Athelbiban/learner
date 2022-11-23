with open('out_1.txt', encoding='utf-8') as inf1,\
        open('out_3.txt') as inf2,\
        open('out_4.txt', 'w', encoding='utf-8') as ouf:
    # for i in inf2:
    #     i = i.split()
    #     i1 = []
    #     for e in i:
    #         e = e.replace('-', '')
    #         i1.append(e)
    #     print(*i1, file=ouf)
    a = set(inf1.read().split('\n'))
    b = set(inf2.read().split('\n'))
    c = b - a
    for i in sorted(c):
        print(i, file=ouf)

