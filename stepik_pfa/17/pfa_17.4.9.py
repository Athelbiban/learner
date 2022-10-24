import random as rnd

with open('files/random.txt', 'w', encoding='utf-8') as ouf:
    for _ in range(25):
        print(rnd.randint(111, 777), file=ouf)
