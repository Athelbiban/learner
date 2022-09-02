def symmetric(n):
    x = [[int(i) for i in input().split()] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if x[i][j] != x[j][i]:
                return 'NO'
    return 'YES'


if __name__ == '__main__':
    print(symmetric(int(input())))
