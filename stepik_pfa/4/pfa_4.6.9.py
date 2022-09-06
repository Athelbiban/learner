n, m = map(int, input().split())
x = [[0] * m for _ in range(n)]
y = iter(list(range(1, n * m + 1)))
row, col, k = 0, 0, 0

while True:
    for i in range(k, 2):
        col = i
        x[row][col] = next(y)
    for i in range(k + 1)