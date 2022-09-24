import random

n = 7
lst = []

while len(lst) < n:
    num = random.randint(1, 49)
    if num not in lst:
        lst.append(num)

print(*sorted(lst))
