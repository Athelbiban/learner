import csv


def parser_training_log(input_file, output_file):
    with open(input_file, encoding='utf-8') as inf, open(output_file, 'w') as ouf:
        writer = csv.writer(ouf, delimiter=',')
        writer.writerow(['train', 'speed', 'error', 'main_record', 'speed_record', 'accuracy_record', 'date'])
        for string in inf:
            if string[:2] == '##':
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
    input_file = '/home/stas/Документы/obsidian/main/журнал тренировки слепой печати.md'
    output_file = 'training_log.csv'
    parser_training_log(input_file, output_file)


if __name__ == '__main__':
    main()
