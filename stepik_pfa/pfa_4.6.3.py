n, m = map(int, input().split())
iterator = iter(range(1, n * m + 1))

# [print(*(str(next(iterator)).ljust(3) for _ in range(m))) for _ in range(n)] # вариант 1

for _ in range(n):      # вариант 2
    for _ in range(m):
        print(str(next(iterator)).ljust(3), end='')
    print()
