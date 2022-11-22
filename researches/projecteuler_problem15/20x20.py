import time


def ways(graph, goal, start='0-0'):
    stack = [(start, [start])]
    s = set()
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]:
            if next == goal:
                # yield tuple(path + [next])
                s.add(tuple(path + [next]))
            else:
                stack.append((next, path + [next]))
    return s


def odd_path(data):
    set_path = set()
    for i in data:
        path_rev = []
        for e in i:
            a, b = e.split('-')
            path_rev.append(f'{b}-{a}')
        path_rev = tuple(path_rev)
        if path_rev in data:
            continue
        else:
            set_path.add(i)
    return set_path


def main():
    n, m = 10, 10
    d = {}
    for i in range(n+1):
        for j in range(m+1):
            if i <= n-1 and j <= m-1:
                d[f'{str(i)}-{str(j)}'] = f'{str(i)}-{str(j + 1)}', f'{str(i + 1)}-{str(j)}'
            elif i <= n-1 and j > m-1:
                d[f'{str(i)}-{str(j)}'] = f'{str(i + 1)}-{str(j)}',
            elif i > n-1 and j <= m-1:
                d[f'{str(i)}-{str(j)}'] = f'{str(i)}-{str(j + 1)}',
            else:
                d[f'{str(i)}-{str(j)}'] = ()
    # return len(ways(d, f'{str(n)}-{str(m)}'))
    a = ways(d, f'{str(n)}-{str(m)}')
    return len(odd_path(a))


if __name__ == '__main__':
    start_time = time.time()
    print(main())
    print(time.time() - start_time)
