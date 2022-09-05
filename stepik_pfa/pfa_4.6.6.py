n = int(input())
[print(*['10'[i > j and i > n + ~j or i < j and i < n + ~j].ljust(3) for i in range(n)]) for j in range(n)]
