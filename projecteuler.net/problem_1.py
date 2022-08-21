"""Задача Эйлера №1:
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9.
Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""

def quantity(value, numb_1, numb_2):
    sum_1 = 0
    sum_2 = 0
    for sign in range(value):
        if sign % numb_1 == 0:
            # print(sign)
            sum_1 += sign
            # print(sum_1)
            if sign % numb_2 == 0:
                sum_1 -= sign
        if sign % numb_2 == 0:
            # print(sign)
            sum_2 += sign
            # print(sum_2)

    return sum_1 + sum_2


print(quantity(1000, 3, 5))
