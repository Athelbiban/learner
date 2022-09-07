n, m = map(int, input().split())
x = [[0] * m for _ in range(n)]
y = iter(list(range(1, n * m + 1)))
row, col, k = 0, 0, 0

while x[-1][-1] == 0 and n <= m:
    if col < n:
        c = col
        for r in range(row, col + 1):
            x[r][c] = str(next(y)).ljust(3)
            c -= 1
    else:
        c = col
        for r in range(row, n):
            x[r][c] = str(next(y)).ljust(3)
            c -= 1
    if col < m - 1:
        col += 1
    else:
        row += 1

while x[-1][-1] == 0 and n > m:
    if col < n and row < 1:
        c = col
        for r in range(row, col + 1):
            x[r][c] = str(next(y)).ljust(3)
            c -= 1
    else:
        c = col
        for r in range(row, m + row):
            x[r][c] = str(next(y)).ljust(3)
            c -= 1
    if col < m - 1:
        col += 1
    else:
        row += 1


for d in x:
    print(*d)
