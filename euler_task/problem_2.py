"""Задача Эйлера №2:
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""

def fibonacci_number_index(index):
    stop_error = "You can't do that!"
    n2 = 0
    n1 = 1
    n = 0
    i = 2
    while i <= index:
        n = n2 + n1
        n2 = n1
        n1 = n
        i += 1
    if index == 0:
        print('?')
        return n2
    elif index == 1:
        return n1
    elif n < 0:

        return stop_error

    return n


def fibonacci_sum_even(value, stop=4000000):
    sum_even = 0
    for i in range(2, value + 2):
        # print(fibonacci_number_index(i))
        if fibonacci_number_index(i) % 2 == 0 and fibonacci_number_index(i) <= stop:
            # print(fibonacci_number_index(i))
            sum_even += fibonacci_number_index(i)
            pass
    return sum_even


print(fibonacci_sum_even(32))
print(fibonacci_number_index(33))
