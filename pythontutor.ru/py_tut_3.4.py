# f = []
# for i in range(8):
#     f.append([int(c) for c in input().split()])
# n = 0
#
# for e in range(n + 1, 8):
#     x1, y1 = f[n]
#     x2, y2 = f[e]
#     if x1 == x2 or y1 == y2:
#         print('YES')
#         break
#     elif abs(x1 - x2) == abs(y1 - y2):
#         print('YES')
#         break
#     n += 1
#
# else:
#     print('NO')


f = []
for i in range(8):
    f.append([int(c) for c in input().split()])
for n in range(8):
    x1, y1 = f[n]
    for e in range(n + 1, 8):
        x2, y2 = f[e]
        if x1 == x2 or y1 == y2:
            print('YES')
            break
        elif abs(x1 - x2) == abs(y1 - y2):
            print('YES')
            break
else:
    print('NO')