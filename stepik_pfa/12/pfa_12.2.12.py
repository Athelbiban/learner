"""
Тайный друг 🌶️

Напишите программу, которая случайным образом назначает каждому ученику
его тайного друга, который будет вместе с ним решать задачи по программированию.

Формат входных данных
На вход программе в первой строке подается число nn – общее количество учеников.
Далее идут nn строк, содержащих имена и фамилии учеников.

Формат выходных данных
Программа должна вывести имя и фамилию ученика (в соответствии с исходным
порядком) и имя и фамилию его тайного друга, разделённые дефисом.

Примечание 1. Обратите внимание, что нельзя быть тайным другом самому себе и
нельзя быть тайным другом для нескольких учеников.

Примечание 2. Приведенные ниже тесты это лишь образцы возможного ответа. Возможны
и другие способы выбора тайных друзей.

Sample Input 1:
3
Светлана Зуева
Аркадий Белых
Борис Боков

Sample Output 1:
Светлана Зуева - Борис Боков
Аркадий Белых - Светлана Зуева
Борис Боков - Аркадий Белых
"""


import random

lst = [input() for _ in range(int(input()))]
lst1, lst2, i = lst.copy(), [], 0

while len(lst2) < len(lst):
    n = random.choice(range(len(lst1)))
    if lst[i] != lst1[n]:
        lst2.append(f'{lst[i]} - {lst1.pop(n)}')
        i += 1
print(*lst2, sep='\n')
