a, b, c, d = int(input()), int(input()), int(input()), int(input())

for i in range(c, d + 1):
    print('\t', i, end='')
print()

for i in range(a, b + 1):
    print(i, end='')
    for e in range(c, d + 1):
        print('\t', i * e, end='')
    print()
