#!/usr/bin/python3


import time


def ways(graph, goal, start='0-0'):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]:
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def main():
    n, m = 11, 11
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
    return ways(d, f'{str(n)}-{str(m)}')


if __name__ == '__main__':
    start_time = time.time()
    for k in main():
        print(*k)
    # print(time.time() - start_time)

