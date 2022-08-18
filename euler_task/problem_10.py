"""Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов."""

import time

start = time.time()

# # Вариант №0:
# def sum_prime(num):
#     summ = 5
#     for i in range(5, num, 2):
#         for e in range(2, int(i ** 0.5) + 1):
#             if not i % e:
#                 break
#         else:
#             summ += i
#     end = time.time()
#     return summ, 'Время выполнения: {:.5f} сек. (~ {:.1f} мин.)'.format((end - start), ((end - start) / 60))


## Вариант №1:
# def sum_prime(num):
#     summ = 0
#     for i in range(2, num):
#         for e in range(2, int(i ** 0.5) + 1):
#             if not i % e:
#                 break
#         else:
#             summ += i
#     end = time.time() - start
#     return summ, end
#
#
# if __name__ == '__main__':
#     print(sum_prime(50))


# Вариант №2:
def sum_prime(num):
    lst = list(range(num + 1))
    for i in range(2, int(num ** 0.5) + 1):
        if lst[i]:
            for e in range(i * i, num + 1, i):
                lst[e] = 0
    end = time.time() - start
    return sum(lst) - 1, end


if __name__ == '__main__':
    print(sum_prime(2_000_000))
