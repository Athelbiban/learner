import csv


with open('/home/stas/Документы/obsidian/main/журнал тренировки слепой печати.md', encoding='utf-8') as inf,\
        open('training_log.csv', 'w') as ouf:
    writer = csv.writer(ouf, delimiter=',')

    for n, _ in enumerate(inf):
        if n == 5:
            break

    for string in inf:
        if string[:2] == '##':
            date = string[3:].rstrip()
        elif string[0].isdigit():
            train, speed, accuracy = string[3:-2].split()
            train = train[:-1]
            accuracy = float(accuracy)
            if speed[0].isdigit():
                speed = int(speed[:-1])
            else:
                speed = int(speed[3:-5])
            writer.writerow([train, speed, accuracy, date])
