n = int(input())
m = [[int(i) for i in input().split()] for _ in range(n)]
max_elem = m[0][0]

for i in range(n):
    for j in range(i + 1):
        if max_elem < m[i][j]:
            max_elem = m[i][j]
print(max_elem)
