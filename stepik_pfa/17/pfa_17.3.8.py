with open('files/data.txt', encoding='utf-8') as inf:
    print(*[i.rstrip() for i in inf.readlines()[::-1]], sep='\n')
