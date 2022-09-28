from fractions import Fraction as F


def inverse_squares(num):
    result = 0
    for i in range(1, num + 1):
        result += F(1, i ** 2)
    return result


if __name__ == '__main__':
    print(inverse_squares(int(input())))
