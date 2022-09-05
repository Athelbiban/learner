n = int(input())
[print(*['01'[i == j or i == n + ~j].ljust(3) for i in range(n)]) for j in range(n)]
