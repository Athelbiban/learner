n, m = map(int, input().split())
table = [[0] * m for _ in range(n)]
checklist = iter(list(range(1, n * m + 1)))
row, col, k = 0, 0, 0

while 0 in table[n // 2]:
    for i in range(k, m - k):
        col = i
        table[row][col] = str(next(checklist)).ljust(3)
    for i in range(k + 1, n - k):
        row = i
        table[row][col] = str(next(checklist)).ljust(3)
    if n > 1 and 0 in table[n // 2]:
        for i in range(m - 2 - k, -1 + k, -1):
            col = i
            table[row][col] = str(next(checklist)).ljust(3)
    if m > 1 and 0 in table[n // 2]:
        for i in range(n - 2 - k, 0 + k, -1):
            row = i
            table[row][col] = str(next(checklist)).ljust(3)
    k += 1

for i in table:
    print(*i)
