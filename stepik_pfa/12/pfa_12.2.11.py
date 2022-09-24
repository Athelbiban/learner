import random

d = iter(random.sample(range(1, 76), 25))
s = [[next(d) for _ in range(5)] for _ in range(5)]
s[2][2] = 0

for n in s:
    for m in n:
        print(str(m).ljust(3), end='')
    print()
