"""Задача Эйлера №5:
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""

# import time
#
# start = time.time()
#
# end = 40
# div = 20
# count = div
# result = 0
#
# while count < end:
#     for div_mod in range(2, div + 1):
#         if end % div_mod != 0:
#             end += div
#             pass
#         pass
#     count += 20
#     result = count
#
# print(result)
#
# end = time.time()
# print('Время выполнения: {:.2f} сек. (~ {:.1f} мин.)'.format((end - start), ((end - start) / 60)))

'''Вариант решения 2. От 01.07.22г.'''

import time

start = time.time()

n = 20
while True:
    for i in range(2, 21):
        if n % i != 0:
            n += 20
            break
    else:
        break
print(n)

end = time.time()
print('Время выполнения: {:.2f} сек. (~ {:.1f} мин.)'.format((end - start), ((end - start) / 60)))
