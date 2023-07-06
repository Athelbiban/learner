from bs4 import BeautifulSoup
import csv
import os


def get_portfolio(input_files, output_file, date=None):
    header = [
        'Наименование', 'ISIN', 'Валюта', 'Количество_нп', 'Номинал_нп',
        'Цена_нп', 'Стоимость_нп', 'НКД_нп', 'Количество_кп',
        'Номинал_кп', 'Цена_кп', 'Стоимость_кп', 'НКД_кп', 'Количество_изп',
        'Стоимость_изп', 'Зачисления', 'Списания', 'Остаток', 'Дата'
    ]
    flag1 = True
    for file, date in zip(input_files, date):
        with open(file) as inf, open(output_file, 'a', encoding='utf-8') as ouf:
            writer = csv.writer(ouf)
            soup = BeautifulSoup(inf.read(), 'html.parser').select('tr')
            flag2 = False
            for string in soup:
                string = string.find_all('td')
                if string[0].text == 'Итого по площадке Фондовый рынок, RUB':
                    break
                if flag2:
                    if string[0].text not in ['Площадка: Фондовый рынок', 'Наименование']:
                        writer.writerow([elem.text.replace(' ', '') for elem in string] + [date])
                if string[0].text == 'Основной рынок':
                    flag2 = True
                    if flag1:
                        writer.writerow(header)
                        flag1 = False


def get_transactions(input_files, output_file):
    header = [
        'Дата заключения', 'Дата расчетов', 'Время', 'Наименование', 'Код',
        'Валюта', 'Вид', 'Количество', 'Цена', 'Сумма', 'НКД', 'Комиссия Брокера',
        'Комиссия Биржи', 'Номер сделки', 'Комментарий', 'Статус'
    ]
    for file in input_files:
        flag1 = True
        n = 0
        with open(file, encoding='utf-8') as inf, open(output_file, 'w', encoding='utf-8') as ouf:
            writer = csv.writer(ouf)
            soup = BeautifulSoup(inf.read(), 'html.parser').select('tr')
            flag2 = False
            for string in soup:
                string = string.find_all('td')
                if string[0].text == 'Итого, RUB':
                    n += 1
                    if n >= 2:
                        break
                if string[0].text == 'Дата заключения':
                    flag2 = True
                if flag2:
                    if string[0].text not in ['Площадка: Фондовый рынок']:
                        writer.writerow([elem.text.replace(' ', '') for elem in string])


def parse_directory(directory):
    return [f'{directory}{node}' for node in sorted(os.listdir(directory))]


def main():
    directory = '/home/stas/Загрузки/broker_report/'
    directory_1 = 'c:\\Users\\VostrovSO\\Downloads\\broker_report\\'
    paths = parse_directory(directory_1)
    out_file_1, out_file_2 = ['portfolio.csv', 'transactions.csv']
    date = [f'20{i[-2:]}-{i[2:4]}-{i[:2]}' for i in [path.split('_')[-2] for path in paths]]
    # get_portfolio(paths, out_file_1, date)
    get_transactions(paths, out_file_2)


if __name__ == '__main__':
    main()
