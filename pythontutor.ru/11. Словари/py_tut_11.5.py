"""
Задача «Права доступа»
Условие
В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам.
Для каждого файла известно, с какими действиями можно к нему обращаться:

запись W,
чтение R,
запуск X.

В первой строке содержится число N — количество файлов содержащихся в данной файловой системе. В следующих
N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами. Далее указано чиcло
M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл. К одному и тому же
файлу может быть применено любое колличество запросов.

Вам требуется восстановить контроль над правами доступа к файлам (ваша программа для каждого запроса должна
будет возвращать OK если над файлом выполняется допустимая операция, или же Access denied, если операция недопустима.
"""


g = {'write': 'W', 'read': 'R', 'execute': 'X'}
d, b = {}, []
for i in range(int(input())):
    s = input().split()
    d[s[0]] = d.get(s[0], s[1:])
for i in range(int(input())):
    s = input().split()
    b.append(s)
for i in range(len(b)):
    for e in range(len(d[b[i][1]])):
        if g[b[i][0]] == d[b[i][1]][e]:
            print('OK')
            break
        elif e == len(d[b[i][1]]) - 1:
            print('Access denied')
