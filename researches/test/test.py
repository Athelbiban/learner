import timeit


def f1():
    # lst = list(range(1_000_000))
    lst = []
    for i in range(1000):
        lst.append(i)
    return lst


def f2():
    lst = [i for i in range(1000)]
    return lst


if __name__ == '__main__':
    x = timeit.repeat(f1, repeat=3, number=100)
    y = timeit.repeat(f2, repeat=3, number=100)

    print(x)
    print(y)
    print(f'Минимальное значение для f1: {min(x)}')
    print(f'Минимальное значение для f2: {min(y)}')
