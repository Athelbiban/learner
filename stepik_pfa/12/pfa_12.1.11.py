import random

n = int(input())    # количество попыток

print(*[random.randint(1, 6) for _ in range(n)], sep='\n')
