"""
Конкатенация файлов 🌶️
На вход программе подается натуральное число n и n строк с названиями файлов.
Напишите программу, которая создает файл output.txt и выводит в него содержимое
всех файлов с указанными именами, не меняя их порядка.

Формат входных данных
На вход программе подается натуральное число n и n строк названий существующих файлов.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.
"""


for _ in range(int(input())):
    with open(f'{input()}', encoding='utf-8') as inf, open('files/output3.txt', 'a', encoding='utf-8') as ouf:
        ouf.write(inf.read())
