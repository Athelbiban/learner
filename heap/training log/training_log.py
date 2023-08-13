import csv
import platform


def creator_csv(input_file, output_file, first_row=None, func=None):
    with open(input_file, encoding='utf-8') as inf, open(output_file, 'w') as ouf:
        writer = csv.writer(ouf, delimiter=',')
        if first_row:
            writer.writerow(first_row)
        if func:
            func(inf, writer)


def writer_training_log(inf, writer, date=None):
    for string in inf:
        if string[0] == '#':
            date = string[3:].rstrip()
        elif string[0].isdigit():
            features = string.rstrip()[3:-1].split()
            writer.writerow(find_record(features) + [date])


def find_record(features):
    main_record = 0
    speed_record = 0
    accuracy_record = 0

    if features[0][0] == "'":
        train = features[0][1:-1]
        main_record = 1
    else:
        train = features[0][:-1]

    if features[1][0] == "'":
        speed = int(features[1][1:-1])
        speed_record = 1
    else:
        speed = int(features[1][:-1])

    if features[2][0] == "'":
        error = float(features[2][1:])
        accuracy_record = 1
    else:
        error = float(features[2])

    return [train, speed, error, main_record, speed_record, accuracy_record]


def main():
    system = platform.system()
    if system == 'Linux':
        directory = '/home/stas/Документы/obsidian/main/журнал тренировки слепой печати.md'
    elif system == 'Windows':
        directory = 'c:\\Users\\VostrovSO\\Downloads\\broker_report\\'
    else:
        raise Exception('Нет директории для данной ОС')

    input_file = directory
    output_file = 'training_log.csv'
    first_row = ['train', 'speed', 'error', 'main_record', 'speed_record', 'accuracy_record', 'date']
    creator_csv(input_file, output_file, first_row, writer_training_log)


if __name__ == '__main__':
    main()
