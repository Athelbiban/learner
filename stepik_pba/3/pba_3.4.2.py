import csv
from collections import Counter


with open('/home/stas/Загрузки/Crimes.csv', 'r') as inf:
    reader = csv.reader(inf)
    headers = next(reader)
    date, prime = headers.index('Date'), headers.index('Primary Type')
    primary_list = []
    for line in reader:
        if line[date].find('2015') != -1:
            primary_list.append(line[prime])

print(*Counter(primary_list).most_common(1)[0])
