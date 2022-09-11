p1 = p2 = p3 = 1

for _ in range(int(input())):
    print(p1, end=' ')
    p1, p2, p3 = p2, p3, p1 + p2 + p3
