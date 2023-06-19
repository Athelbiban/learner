import csv


def parser_training_log(input_file, output_file):
    with open(input_file, encoding='utf-8') as inf, open(output_file, 'w') as ouf:
        writer = csv.writer(ouf, delimiter=',')
        writer.writerow(['train', 'speed', 'accuracy', 'record', 'date'])
        for n, _ in enumerate(inf):
            if n == 5:
                break
        for string in inf:
            if string[:2] == '##':
                date = string[3:].rstrip()
            elif string[0].isdigit():
                features = string[3:-2].split()
                writer.writerow(find_record(features) + [date])


def find_record(features, record=''):
    for i, f in enumerate(features):
        if i == 0:
            if f[0] == "'":
                train = f[1:-1]
                record += 'm'
            else:
                train = f[:-1]
        elif i == 1:
            if f[0] == "'":
                speed = int(f[1:-1])
                record += 's'
            else:
                speed = int(f[:-1])
        else:
            if f[0] == "'":
                accuracy = float(f[1:])
                record += 'a'
            else:
                accuracy = float(f)
    return [train, speed, accuracy, record]


def main():
    input_file = '/home/stas/Документы/obsidian/main/журнал тренировки слепой печати.md'
    output_file = 'training log/training_log.csv'
    parser_training_log(input_file, output_file)


if __name__ == '__main__':
    main()
