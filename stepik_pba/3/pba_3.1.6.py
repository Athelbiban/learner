s, a, b = (input() for _ in '...')
n = 0

while n <= 1000:
    if a in s:
        s = s.replace(a, b)
        n += 1
    else:
        print(n)
        break
else:
    print('Impossible')
