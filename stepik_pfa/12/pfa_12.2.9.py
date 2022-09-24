import random

print(*random.sample(range(int(1e6), int(1e7)), 100), sep='\n')
