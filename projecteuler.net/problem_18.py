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

# res = 0
# for i in m.strip().split('\n'):
#     res += max(map(int, i.split()))
# print(res)
d = [[int(e) for e in i.split()] for i in m.strip().split('\n')]
print(d)


def path(data, i, j, path=None):
    if path is None:
        path = []
    q = [data[i][j]]
    # while q:
    #     v = q.pop()
    #     path = path + [v]
    #     if data[i+1:i+2]:
    #         i += 1
    #         q += [data[i][j]] + [data[i][j+1]]
    #         j += 1
    # return path


def way(data, i=0, j=0, start=None):
    if start is None:
        start = data[i][j]
    # while i < len(data):
    #     res = start

    return path(data, i, j)


if __name__ == '__main__':
    print(way(d))
