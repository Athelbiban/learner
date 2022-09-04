n, m = int(input()), int(input())
lst = [[input() for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(lst[i][j], end=' ')
    print()
