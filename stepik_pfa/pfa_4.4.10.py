n = int(input())
m = [[int(i) for i in input().split()] for _ in range(n)]
print(sum(m[i][i] for i in range(n)))
