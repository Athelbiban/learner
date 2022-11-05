def is_parent(child, path=None):
    if path is None:
        path = set()
    path.add(child)
    if child in data and data[child]:
        for node in data[child]:
            if node not in path:
                path |= is_parent(node)
    return path


data = {}
for _ in range(int(input())):
    lst = input().split()
    data[lst[0]] = lst[2:]

except_set = set()
for _ in range(int(input())):
    exception = input()
    parents = is_parent(exception)
    for sample in except_set:
        if sample in parents:
            print(exception)
            break
    else:
        except_set.add(exception)
