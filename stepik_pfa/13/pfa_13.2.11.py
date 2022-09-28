from fractions import Fraction as F


def inverse_factorial(num):
    a = 1
    if num == 1:
        return num
    else:
        for i in range(1, num + 1):
            a *= i
    return F(1, a) + inverse_factorial(num - 1)


if __name__ == '__main__':
    print(inverse_factorial(int(input())))
