def build_query_string(params):
    lst = sorted([i for i in params.keys()])
    t = []
    for i in lst:
        t += [f'{i}={params[i]}']
    return '&'.join(t)


if __name__ == '__main__':
    print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
