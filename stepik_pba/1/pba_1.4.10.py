def workspaces(get_list):
    d = {'global': {'a': {}, 'foo': {}}}
    for func, name1, name2 in get_list:
        def add(namespace, var, n):

            if namespace in n:

            return add(d[namespace], var)
        # if func == 'add':
    #         d['global'].setdefault(name1, name2)
    #     elif func == 'create':

    return d


if __name__ == '__main__':
    print(workspaces([input().split() for _ in range(int(input()))]))
