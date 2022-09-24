import random

n = int(input())
[print(('Решка', 'Орел')[random.randrange(2)]) for _ in range(n)]
