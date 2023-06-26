from bs4 import BeautifulSoup
import csv


def broker_report_html_to_csv(input_files, output_file):
    for file in input_files:
        with open(file) as inf, open(output_file, 'w', encoding='utf-8') as ouf:
            writer = csv.writer(ouf)
            soup = BeautifulSoup(inf.read(), 'html.parser').select('tr')
            flag = False
            for string in soup:
                string = string.find_all('td')
                if string[0].text == 'Итого по площадке Фондовый рынок, RUB':
                    break
                if flag:
                    if string[0].text not in ['Площадка: Фондовый рынок']:
                        writer.writerow([elem.text for elem in string])
                if string[0].text == 'Основной рынок':
                    flag = True


def main():
    in_files = 'S03DNRY_160623_160623_D.html'
    out_file = 'parser_broker_report.csv'
    broker_report_html_to_csv([in_files], out_file)


if __name__ == '__main__':
    main()
