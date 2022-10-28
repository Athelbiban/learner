def workspaces(get_list):
    global d
    func, name1, name2 = get_list

    def add(namespace, var):
        d[namespace]['var'].add(var)

    def create(namespace, parent):
        d.setdefault(namespace, {'var': set(), 'parent': parent})

    def get(namespace, var):
        if namespace is None or var in d[namespace]['var']:
            return print(namespace)
        return get(d[namespace]['parent'], var)

    if func == 'add':
        add(name1, name2)
    elif func == 'create':
        create(name1, name2)
    else:
        get(name1, name2)


if __name__ == '__main__':
    d = {'global': {'var': set(), 'parent': None}}
    for lst in [input().split() for _ in range(int(input()))]:
        workspaces(lst)
