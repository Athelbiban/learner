with open(r'write_here.txt', 'w', encoding='utf-8') as ouf:
    n = 0
    for i in range(255):
        ouf.write('Stas ')
        n += 1
        if not n % 15:
            ouf.write('\n')
