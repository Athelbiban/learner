n, m = [int(i) for i in input().split()]
lst = [list(input()) for _ in range(n)]

for i in range(n):
    for e in range(m):
        if lst[i][e] == '.':
            counter = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if n - 1 >= i + x >= 0 and m - 1 >= e + y >= 0 and lst[i + x][e + y] == '*':
                        counter += 1
            lst[i][e] = str(counter)

for s in lst:
    print(*s, sep='')
