"""
Задача «Больше предыдущего»
Условие
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента
"""


s = input().split()
for i in range(1, len(s)):
    if int(s[i]) > int(s[i-1]):
        print(s[i], end=' ')
