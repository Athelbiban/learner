n = int(input())
m = [[int(e) for e in input().split()] for _ in range(n)]
sum_top, sum_right, sum_bottom, sum_left = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if i < j and (i > n - j - 1):
            sum_right += m[i][j]
        elif i > j and (i > n - j - 1):
            sum_bottom += m[i][j]
        elif i > j and (i < n - j - 1):
            sum_left += m[i][j]
        elif i < j and (i < n - j - 1):
            sum_top += m[i][j]

print(f'Верхняя четверть: {sum_top}',
      f'Правая четверть: {sum_right}',
      f'Нижняя четверть: {sum_bottom}',
      f'Левая четверть: {sum_left}', sep='\n')
