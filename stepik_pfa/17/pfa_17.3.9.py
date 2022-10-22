with open('files/lines1.txt', encoding='utf-8') as inf:
    lines = inf.read().split('\n')
    max_len = max(map(len, lines))
    print(*filter(lambda x: len(x) == max_len, lines), sep='\n')
