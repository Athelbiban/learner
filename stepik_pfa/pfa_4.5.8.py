t = 8
j, i = input()
i, j = t - int(i), ord(j) - 97
x = [['.'] * t for _ in range(t)]
x[i][j] = 'N'
knight_move = (j + 2, i + 1), (j + 2, i - 1), (j - 2, i + 1), (j - 2, i - 1),\
              (j + 1, i + 2), (j - 1, i + 2), (j + 1, i - 2), (j - 1, i - 2)

for n, m in knight_move:
    if 0 <= m < t and 0 <= n < t:
        x[m][n] = '*'

for row in x:
    print(*row)
