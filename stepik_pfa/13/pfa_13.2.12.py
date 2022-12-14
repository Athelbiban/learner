"""
Юный математик 🌶️

Дима учится в седьмом классе и сейчас они проходят обыкновенные дроби с натуральными
числителем и знаменателем. Вчера на уроке математики Дима узнал, что дробь называется
правильной, если ее числитель меньше знаменателя, и несократимой, если нет равной ей
дроби с меньшими натуральными числителем и знаменателем.

Дима очень любит математику, поэтому дома он долго экспериментировал, придумывая и
решая разные задачки с правильными несократимыми дробями. Одну из этих задач Дима
предлагает решить вам с помощью компьютера.

На вход программе подается натуральное число n. Напишите программу, которая находит
наибольшую правильную несократимую дробь с суммой числителя и знаменателя равной n.

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить
наибольший общий делитель (НОД) двух чисел. Функция реализована в модуле math.

Sample Input 1:
10

Sample Output 1:
3/7
"""


from math import gcd
from fractions import Fraction as F

den = int(input())

for num in range(den // 2, 0, -1):
    if gcd(num, den - num) == 1:
        print(F(num, den - num))
        break
