## Печать элементов сразу, не используя хранение элементов списка.
# n = int(input())
# counter = 0
#
# for i in range(1, n + 1):
#     for _ in range(i):
#         if counter < n:
#             print(i, end=' ')
#             counter += 1


# # Список представляющий собой заданную последовательность,
# # после чего выводящий прервый n элементов.
# n = int(input())
# lst = []
#
# for k in range(1, n + 1):
#     for _ in range(k):
#         lst.append(k)
# print(lst[:n])


# Функция-генератор которая создаёт бесконечную последовательность,
# и выводит только n членов этой последовательности.
def infinite_sequence(n):
    counter = 0
    for i in range(1, n + 1):
        k = 0
        while counter < n and k < i:
            counter += 1
            k += 1
            yield i


if __name__ == '__main__':
    print(*infinite_sequence(10))
