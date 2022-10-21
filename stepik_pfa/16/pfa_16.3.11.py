"""
IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающий по протоколу TCP/IP.

В 44-й версии IP-адрес представляет собой 3232-битное число. Адрес записывается в виде четырёх
десятичных чисел (октетов) со значением от 00 до 255255, разделённых точками, например, 192.168.1.2192.168.1.2.

Напишите программу, которая считывает IP-адреса и выводит их в порядке возрастания в
соответствии с десятичным представлением.

Формат входных данных
На вход программе подается число n (n≥1) – количество IP-адресов. Затем n
строк с корректными IP-адресами.

Формат выходных данных
Программа должна вывести IP-адреса в порядке возрастания в соответствии с десятичным представлением.

Примечание 1. Чтобы перевести IP-адрес 192.168.1.2 в десятичное число мы используем формулу:

192 * 256^3 + 168 * 256^2 + 1 * 256^1 + 2 * 256^0 = 3232235778

Примечание 2. Используйте необязательный аргумент key.


Sample Input:

9
128.199.44.24
128.199.201.245
143.198.168.95
172.67.181.62
172.67.222.111
172.67.10.90
45.8.106.59
203.13.32.156
172.67.181.194
Sample Output:

45.8.106.59
128.199.44.24
128.199.201.245
143.198.168.95
172.67.10.90
172.67.181.62
172.67.181.194
172.67.222.111
203.13.32.156
"""


print(*sorted([input() for _ in range(int(input()))],
              key=lambda x: sum([int(i)*256**(abs(x.split('.').index(i) - 3)) for i in x.split('.')])), sep='\n')
