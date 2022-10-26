def c(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return c(n-1, k) + c(n-1, k-1)


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(c(n, k))
