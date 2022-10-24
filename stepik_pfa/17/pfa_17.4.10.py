with open('files/input.txt', encoding='utf-8') as inf, open('files/output1.txt', 'w', encoding='utf-8') as ouf:
    for i, line in enumerate(inf, 1):
        print(f'{i})', line.rstrip(), file=ouf)
