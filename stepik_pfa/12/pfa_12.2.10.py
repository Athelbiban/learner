import random

s = list(input())
random.shuffle(s)
print(*s, sep='')
