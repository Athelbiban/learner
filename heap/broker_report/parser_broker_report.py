from bs4 import BeautifulSoup
import csv


with open('S03DNRY_160623_160623_D.html') as inf, open('parser_broker_report.csv', 'w', encoding='utf-8') as ouf:
    writer = csv.writer(ouf)
    soup = BeautifulSoup(inf.read(), 'html.parser').select('tr')
    flag = False
    for string in soup:
        string = string.find_all('td')
        if string[0].text == 'Основной рынок':
            flag = True
        if string[0].text == 'Итого по площадке Фондовый рынок, RUB':
            break
        if flag:
            if string[0].text != 'Основной рынок' and string[0].text != 'Площадка: Фондовый рынок':
                writer.writerow([k.text for k in string])
