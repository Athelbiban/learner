from fractions import Fraction as f
from math import gcd

n = int(input())
lst = []

for i in range(1, n + 1):
    for j in range(n, i, -1):
        if gcd(i, j) == 1:
            lst.append(f(i, j))
print(*sorted(lst), sep='\n')
