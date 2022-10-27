def namespaces(get_list):
    # d = {'global': {}}
    # for func, name1, name2 in get_list:
    #     if func == 'add':
    #         d['global'].setdefault(name1, name2)
    #     elif func == 'create':

    return d


if __name__ == '__main__':
    print(namespaces([input().split() for _ in range(int(input()))]))
