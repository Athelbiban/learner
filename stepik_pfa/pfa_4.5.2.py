n, m = int(input()), int(input())
x = [[int(e) for e in input().split()] for _ in range(n)]
max_elem = x[0][0], 0, 0

for i in range(n):
    for j in range(m):
        if max_elem[0] < x[i][j]:
            max_elem = x[i][j], i, j

print(max_elem[1], max_elem[2])
