## Печать элементов сразу, не используя хранение элементов списка.
# n = int(input())
# counter = 0
#
# for i in range(1, n + 1):
#     for _ in range(i):
#         if counter < n:
#             print(i, end=' ')
#             counter += 1


# Список представляющий собой заданную последовательность,
# после чего выводящий прервый n элементов.
n = int(input())
lst = []

for k in range(1, n + 1):
    for _ in range(k):
        lst.append(k)
print(lst[:n])
