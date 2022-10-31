"""
Лог файл 🌶️
Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя
в систему и выхода из нее. Каждая строка файла содержит три значения, разделенные
запятыми и символом пробела: имя пользователя, время входа, время выхода, где
время указано в 2424-часовом формате.

Напишите программу, которая создает файл output.txt и выводит в него имена всех
пользователей (не меняя порядка следования), которые были в сети не менее часа.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Считайте, что каждый пользователь был только раз в системе, то есть в
файле нет двух строк с одинаковым пользователем.

Примечание 3. Если бы файл logfile.txt содержал строки:

Тимур Гуев, 14:10, 15:50
Руслан Гриценко, 12:00, 12:59
Роман Гацалов, 09:10, 17:45
Габолаев Георгий, 11:10, 12:10
то файл output.txt имел бы вид:

Тимур Гуев
Роман Гацалов
Габолаев Георгий
"""


with open('files/logfile.txt', encoding='utf-8') as inf, open('files/output2.txt', 'w', encoding='utf-8') as ouf:
    for line in inf:
        lst = line.rstrip().split(', ')
        time_start = [int(h)*60 + int(m) for h, m in [lst[1].split(':')]][0]
        time_end = [int(h)*60 + int(m) for h, m in [lst[2].split(':')]][0]
        if time_end - time_start >= 60:
            print(lst[0], file=ouf)