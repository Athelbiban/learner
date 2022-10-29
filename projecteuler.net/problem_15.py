import random as rnd
from time import time

start = time()


def way(n):
    lst = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    lst_inv = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    i, j = 0, 0
    lst[i][j], lst_inv[j][i] = 1, 1
    while i + j != 2 * n:
        x, y = rnd.choice(((0, 1), (1, 0)))
        if i + x <= n and j + y <= n:
            i, j = i + x, j + y
            lst[i][j] = 1
            lst_inv[j][i] = 1
    return lst, lst_inv


def main():
    n = 9
    ways = []
    for _ in range(750_000):
        w, w_inv = way(n)
        if w not in ways:
            ways.append(w)
            ways.append(w_inv)
    # for k in ways:
        # print(*k, sep='\n')
    # print(ways)
    print(len(ways))


if __name__ == '__main__':
    main()
print(time()-start)
