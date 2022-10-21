"""
Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой.

Функция должна получать на вход один обязательный аргумент data – список, который
следует вывести и два необязательных строковых односимвольных  аргумента side и
delimiter и выводить содержимое списка в соответствии с примерами.

В случае если отсутствует аргумент side, то полагаем side='-', а если отсутствует
аргумент delimiter, то полагаем delimiter='|'.

Примечание 1. Следующий программный код:

pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
должен выводить:

 ------------------------------
| 1 | 2 | 10 | 23 | 123 | 3000 |
 ------------------------------
 -------------------------
| abc | def | ghi | 12345 |
 -------------------------
 *****************
| abc | def | ghi |
 *****************
 -----------------
# abc # def # ghi #
 -----------------
 *****************
# abc # def # ghi #
 *****************
"""


def pretty_print(data, side='-', delimiter='|'):
    string = f' {delimiter} '.join(map(str, data))
    print(' ' + side * len(string) + 2 * side + ' ')
    print(delimiter, end=' ')
    print(string, end=' ')
    print(delimiter)
    print(' ' + side * len(string) + 2 * side + ' ')


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
