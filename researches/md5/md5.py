import csv


code = {
    ' СБ': 'Сборочный чертёж',
    ' Е1': 'Схема деления структурная',
    ' Э3': 'Схема электрическая принципиальная',
    'ПЭ3': 'Перечень элементов',
    ' ТБ': 'Таблица соединений',
    ' ВП': 'Ведомость покупных изделий',
    ' МЧ': 'Монтажный чертёж'
}

with open(r'1ВЛ.md5', encoding='utf-8') as inf, open(r'test.csv', 'w', encoding='utf-8') as ouf:
    for row in inf:
        row1 = row.split(maxsplit=1)
        row2, row3 = row1[1].split(' _ ')
        decimal, name = row2[1:], row3[:-5]
        md5 = row1[0]
        decimal_code = decimal[-3:]
        if not decimal_code.isdigit():
            if decimal_code in code:
                name = f'{name} {code[decimal_code]}'
        lst = [md5, decimal, name]
        wr = csv.writer(ouf, delimiter='\t', lineterminator='\r')
        wr.writerow(lst)
