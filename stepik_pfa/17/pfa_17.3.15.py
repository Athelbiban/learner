def read_csv():
    with open('files/data.csv', encoding='utf-8') as inf:
        first_line = inf.readline().rstrip().split(',')
        list_of_dict = []
        for line in inf:
            dict_temp = {}
            for i, val in enumerate(line.rstrip().split(',')):
                dict_temp[first_line[i]] = val
            list_of_dict.append(dict_temp)
        return list_of_dict


if __name__ == '__main__':
    print(read_csv())
