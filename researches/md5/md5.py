import csv


with open(r'file.txt', encoding='utf-8') as inf, open(r'test.csv', 'w', encoding='utf-8') as ouf:
    for row in inf:
        row1 = row.split(maxsplit=1)
        row2, row3 = row1[1].split('_')
        decimal, name = row2[1:-1], row3[1:-5]
        md5 = row1[0]
        if not decimal[-3:].isdigit():
            if decimal[-3:] == ' СБ':
                name = f'{name} Сборочный чертёж'
            elif decimal[-3:] == 'ПЭ3':
                name = f'{name} Перечень элементов'
        lst = [md5, decimal, name]
        wr = csv.writer(ouf, delimiter=',')
        wr.writerow(lst)
