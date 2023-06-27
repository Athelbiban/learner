from bs4 import BeautifulSoup
import csv
import os


def broker_report_html_to_csv(input_files, output_file, date=None):
    header = ['Наименование', 'ISIN', 'Валюта', 'Количество (нп)', 'Номинал (нп)',
              'Цена (нп)', 'Стоимость (нп)', 'НКД (нп)', 'Количество (кп)',
              'Номинал (кп)', 'Цена (кп)', 'Стоимость (кп)', 'НКД (кп)', 'Количество (изп)',
              'Стоимость (изп)', 'Зачисления', 'Списания', 'Остаток', 'Дата']
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
                        writer.writerow([float(elem.text.replace(' ', '')) if elem.text.replace(' ', '').isdigit() else elem.text for elem in string] + [date])
                if string[0].text == 'Основной рынок':
                    flag2 = True
                    if flag1:
                        writer.writerow(header)
                        flag1 = False


def parse_directory(directory):
    return [f'{directory}{node}' for node in sorted(os.listdir(directory))]


def main():
    directory = '/home/stas/Загрузки/broker_report/'
    paths = parse_directory(directory)
    out_file = 'parser_broker_report.csv'
    date = [f'20{i[-2:]}-{i[2:4]}-{i[:2]}' for i in [path.split('_')[-2] for path in paths]]
    broker_report_html_to_csv(paths, out_file, date)


if __name__ == '__main__':
    main()
