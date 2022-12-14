"""
Каждый n-ый элемент
На вход программе подается строка текста, содержащая символы и число n. Из данной
строки формируется список. Напишите программу, которая разделяет список
на вложенные подсписки так, что nn последовательных элементов принадлежат разным подспискам.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные
символом пробела и число nn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Графическая иллюстрация для 11 теста:

https://ucarecdn.com/63705c1f-3e12-4a8e-a3ae-815aecbb9233/

Sample Input 1:
a b c d e f g h i j k l m n
3

Sample Output 1:
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""


lst, n = input().split(), int(input())
res = [[] * n for _ in range(n)]

for i in range(n):
    for e in range(i, len(lst), n):
        res[i].extend(lst[e])
print(res)
