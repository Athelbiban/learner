code = input()
d = {int(k): v for _ in range(int(input())) for v, k in [input().split(': ')]}
[print(d[code.count(i)], end='') for i in code]
