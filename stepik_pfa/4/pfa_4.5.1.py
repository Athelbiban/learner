n, m = int(input()), int(input())
mult = [[i * j for i in range(m)] for j in range(n)]

for row in mult:
    for num in row:
        print(str(num).ljust(3), end=' ')
    print()
