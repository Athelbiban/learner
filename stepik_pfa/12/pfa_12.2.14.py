"""
Генератор паролей 2 🌶️

Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов,
состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).

Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна
цифра и как минимум по одной букве в верхнем и нижнем регистре.

Формат входных данных
На вход программе подаются два числа n и m, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести nn паролей длиной mm символов в соответствии с условием
задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли
сгенерировать возможно.

Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:

функция generate_password(length) – возвращает случайный пароль длиной length символов;
функция generate_passwords(count, length) – возвращает список, состоящий из
count случайных паролей длиной length символов.
Примечание 3. Приведенные ниже тесты – это лишь образцы возможного ответа.
Возможны и другие способы генерации паролей.

Sample Input 1:
9
7

Sample Output 1:
iHnPg7q
Njj9m3N
tQ9v5ut
6qPZ3tV
6gVScya
kU8ncAY
5CKX9Da
UTQRve4
FyRe8NN
"""


import random
import string


def generate_password(length):
    password = []
    password.extend(random.choice(char) for char in (low, up, dig))
    password.extend(random.choice(low_up_dig) for _ in range(length - 3))
    random.shuffle(password)
    return ''.join(password)


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


if __name__ == '__main__':
    low = tuple(set(string.ascii_lowercase) - set('lo'))
    up = tuple(set(string.ascii_uppercase) - set('IO'))
    dig = tuple(set(string.digits) - set('10'))
    low_up_dig = low + up + dig
    print(*generate_passwords(int(input()), int(input())), sep='\n')
