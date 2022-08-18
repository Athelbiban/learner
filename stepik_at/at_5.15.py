def simple_continued_fraction(n, d):
    lst = []
    while d:
        a = n // d
        lst.append(a)
        d, n = n % d, d
    return lst


def main():
    a, b = map(int, input().split('/'))
    return simple_continued_fraction(a, b)


if __name__ == '__main__':
    print(*main())
