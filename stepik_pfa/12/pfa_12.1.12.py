import random

length = int(input())

while length:
    n = random.randint(65, 122)
    if n <= 90 or n >= 97:
        print(chr(n), end='')
        length -= 1
