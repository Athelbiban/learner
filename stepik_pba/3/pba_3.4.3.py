import json


def depth(node, data, path=None):
    if path is None:
        path = set()
    path |= data[node]
    for par in data[node]:
        path |= depth(par, data)
    return path


dict_set = {i['name']: set(i['parents']) for i in json.loads(input())}
dict_depth = {i: depth(i, dict_set) for i in dict_set}

dict_count = {}
for k in dict_depth:
    count = 1
    for j in dict_depth:
        if k in dict_depth[j]:
            count += 1
    dict_count[k] = dict_count.get(k, count)

for x, y in sorted(dict_count.items()):
    print(f'{x} : {y}')
