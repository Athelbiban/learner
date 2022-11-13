import time

st = time.time()
m = """
3
7 4
2 4 6
8 5 9 3
"""
n = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
t = [[e for e in i.split()] for i in n.strip().split('\n')]
d = {}
for i, _ in enumerate(t):
    for j, _ in enumerate(t[i]):
        if t[i+1:i+2]:
            d[f'{str(i)}{str(j)}-{str(t[i][j])}'] = f'{str(i+1)}{str(j)}-{str(t[i+1][j])}', \
                                                    f'{str(i+1)}{str(j+1)}-{str(t[i+1][j+1])}'
        else:
            d[f'{str(i)}{str(j)}-{str(t[i][j])}'] = tuple()
start = f'00-{t[0][0]}'
len_t1 = len(t) - 1
end = [f'{str(len_t1)}{str(k)}-{str(t[len_t1][k])}' for k in range(len(t[-1]))]


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]:
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def main():
    max_way = []
    max_cost = 0
    for i in end:
        for e in dfs_paths(d, start, i):
            w1 = 0
            for u in e:
                w1 += int(u.split('-')[-1])
            if w1 > max_cost:
                max_cost = w1
                max_way = e
    return max_cost, max_way


if __name__ == '__main__':
    print(main())
print(time.time() - st)
