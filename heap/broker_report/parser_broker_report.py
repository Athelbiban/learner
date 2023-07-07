from bs4 import BeautifulSoup
import csv
import os
import re


def get_portfolio(input_files, output_file, date=None):
    header = [
        'Наименование', 'ISIN', 'Валюта', 'Количество_нп', 'Номинал_нп',
        'Цена_нп', 'Стоимость_нп', 'НКД_нп', 'Количество_кп',
        'Номинал_кп', 'Цена_кп', 'Стоимость_кп', 'НКД_кп', 'Количество_изп',
        'Стоимость_изп', 'Зачисления', 'Списания', 'Остаток', 'Дата'
    ]
    flag1 = True
    for file, date in zip(input_files, date):
        with open(file, encoding='utf-8') as inf,\
                open(output_file, 'a', encoding='utf-8', newline='') as ouf:
            writer = csv.writer(ouf)
            soup = BeautifulSoup(inf.read(), 'html.parser').select('tr, p')
            flag2 = False
            for string in soup:
                if re.search(r'Портфель Ценных Бумаг', string.text):
                    flag2 = True
                elif re.search(r'Итого', string.text):
                    flag2 = False
                if flag2:
                    string = string.find_all('td')
                    if flag1:
                        writer.writerow(header)
                        flag1 = False
                    if string and string[0].text not in ['Основной рынок', 'Наименование', 'Площадка: Фондовый рынок']:
                        writer.writerow([elem.text.replace(' ', '') for elem in string] + [date])


def get_transactions(input_files, output_file):
    header = [
        'Дата заключения', 'Дата расчетов', 'Время', 'Наименование', 'Код',
        'Валюта', 'Вид', 'Количество', 'Цена', 'Сумма', 'НКД', 'Комиссия Брокера',
        'Комиссия Биржи', 'Номер сделки', 'Комментарий', 'Статус'
    ]
    flag1 = True
    for file in input_files:
        with open(file, encoding='utf-8') as inf,\
                open(output_file, 'a', encoding='utf-8', newline='') as ouf:
            writer = csv.writer(ouf)
            soup = BeautifulSoup(inf.read(), 'html.parser').select('tr, p')
            flag2 = False
            for string in soup:
                if re.search(r'Сделки купли/продажи', string.text):
                    flag2 = True
                elif re.search(r'Итого', string.text):
                    flag2 = False
                if flag2:
                    string = string.find_all('td')
                    if flag1:
                        writer.writerow(header)
                        flag1 = False
                    if string and string[0].text not in ['Дата заключения', 'Площадка: Фондовый рынок']:
                        writer.writerow(elem.text.replace(' ', '') for elem in string)


def parse_directory(directory):
    return [f'{directory}{node}' for node in sorted(os.listdir(directory))]


def main():
    directory_unix = '/home/stas/Загрузки/broker_report/'
    directory_win = 'c:\\Users\\VostrovSO\\Downloads\\broker_report\\'
    paths = parse_directory(directory_win)
    out_file_1, out_file_2 = ['portfolio.csv', 'transactions.csv']
    date = [f'20{i[-2:]}-{i[2:4]}-{i[:2]}' for i in [path.split('_')[-2] for path in paths]]
    get_portfolio(paths, out_file_1, date)
    get_transactions(paths, out_file_2)


if __name__ == '__main__':
    # 1. Дописать функцию удаляющую в директориях out_file_1
    # и out_file_2 файлы portfolio.csv и transactions.csv
    # 2. Убрать дублирующий код в методах get_portfolio и get_transactions
    main()
