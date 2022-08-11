s, n = input().split(), input()
print(*[i for i, e in enumerate(s) if e == n] or ['None'])

# print(*[i for i, e in enumerate(s) if e == n] if n in s else [None])

# c = 0
# for i, e in enumerate(s):
#     if e == n:
#         print(i, end=' ')
#         c += 1
# if c == 0:
#     print('None')
