# def transpose(a, b):
#     s = []
#     res = []
#     counter = 0
#     while counter < int(a):
#         s.append(input().split())
#         counter += 1
#     for k in range(int(b)):
#         c = []
#         for w in range(int(a)):
#             c.append(s[w][k])
#         res.append(c)
#
#     return zip(res)
#
#
# n, m = input().split()
#
# for t in transpose(n, m):
#     print(' '.join(*t))


n, m = list(map(int, input().split()))
list(map(print, *(input().split() for q in range(n))))