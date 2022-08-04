# Вариант 1:
lst, x = input().split(), input()
print(*[i for i, e in enumerate(lst) if e == x] or ['Отсутствует'])


# # Вариант 2 (работает):
# lst, x = input().split(), input()
#
# for i, e in enumerate(lst):
#     if x not in lst:
#         print('Отсутствует')
#         break
#     elif e == x:
#         print(i, end=' ')
