"""Задача Эйлера №4:
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""

import time

start = time.time()

number_1 = 999
number_2 = 999


def is_palindrome(num):
    number_str = str(num)
    number_invert = int(number_str[::-1])
    if num == number_invert:
        return True
    else:
        return False


def largest_palindrome(num_1, num_2):
    num_1_end_str = str(num_1)
    num_2_end_str = str(num_2)
    counter_1 = 0
    counter_2 = 0
    for i in num_1_end_str:
        counter_1 += 1
    num_1_end = int('1' + '0' * (counter_1 - 1))
    for i in num_2_end_str:
        counter_2 += 1
    num_2_end = int('1' + '0' * (counter_2 - 1))

    list_palindrome = []

    for enumeration_num_1 in range(num_1, num_1_end, -1):
        for enumeration_num_2 in range(num_2, num_2_end, -1):
            result_01 = enumeration_num_1 * enumeration_num_2
            if is_palindrome(result_01):
                list_palindrome += [result_01]
                break
    return sorted(list_palindrome, reverse=True)[0]


result = largest_palindrome(number_1, number_2)

print(result)

end = time.time()
print('Время выполнения: {:.2f} сек. (~ {:.1f} мин.)'.format((end - start), ((end - start) / 60)))
