import time


def ways(graph, goal, start='00'):
    stack = [(start, [start])]
    # count = 0
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]:
            if next == goal:
                yield tuple(path + [next])
                # count += 1
            else:
                stack.append((next, path + [next]))
    # return count


def odd_path(data):
    set_path = set()
    # while data:
    for i in data:
        path_rev = []
        for e in i:
            l = len(e)
            if l == 2:
                path_rev.append(e[::-1])
            else:
                path_rev.append(e[l//2:] + e[:l//2])
        path_rev = tuple(path_rev)
        if path_rev in data:
            # i = i,
            # path_rev = path_rev,
            # data = data - set(i) - set(path_rev)
            # break
            continue
        else:
            set_path.add(i)
            # return lst
    return set_path


def main():
    n, m = 12, 12
    d = {}
    for i in range(n+1):
        for j in range(m+1):
            if i <= n-1 and j <= m-1:
                d[f'{str(i)}{str(j)}'] = f'{str(i)}{str(j + 1)}', f'{str(i + 1)}{str(j)}'
            elif i <= n-1 and j > m-1:
                d[f'{str(i)}{str(j)}'] = f'{str(i + 1)}{str(j)}',
            elif i > n-1 and j <= m-1:
                d[f'{str(i)}{str(j)}'] = f'{str(i)}{str(j + 1)}',
            else:
                d[f'{str(i)}{str(j)}'] = ()
    # return ways(d, f'{str(n)}{str(m)}')
    a = set(ways(d, f'{str(n)}{str(m)}'))
    return len(odd_path(a))


if __name__ == '__main__':
    start_time = time.time()
    print(main())
    print(time.time() - start_time)
