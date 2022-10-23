with open('files/numbers1.txt', encoding='utf-8') as inf:
    for line in inf:
        print(sum(map(int, line.split())))
