"""
В римской системе счисления для обозначения чисел используются следующие символы
(справа записаны числа, которым они соответствуют в десятичной системе счисления):

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Будем использовать вариант, в котором числа 4, 9, 40, 90, 400 и 900 записываются
как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.

Формат ввода:
Строка, содержащая натуральное число n, 0 < n < 4000.

Формат вывода:
Строка, содержащая число, закодированное в римской системе счисления.

Sample Input 1:
1984

Sample Output 1:
MCMLXXXIV
"""


def decimal_number(num, s, roman=''):
    if num == 0:
        return roman
    else:
        for k in s:
            if k <= num:
                return decimal_number(num - k, s, roman + s[k])


def main(n):
    s = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
         50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    number_roman = ''
    for i, e in enumerate(reversed(n)):
        number = int(e) * 10 ** i
        number_roman = decimal_number(number, s) + number_roman
    return number_roman


if __name__ == '__main__':
    print(main(input()))
