# s, temp = set(), []
#
# for i in sorted(input().split()):
#     if i not in temp:
#         temp.append(i)
#     else:
#         s.add(i)
# print(*s)


# lst, s = input().split(), set()
#
# for i in lst:
#     if lst.count(i) > 1:
#         s.add(i)
# print(*s)


# lst = input().split()
# print(*set(filter(lambda i: lst.count(i) > 1, lst)))


lst = input().split()
print(*set([i for i in lst if lst.count(i) > 1]))
