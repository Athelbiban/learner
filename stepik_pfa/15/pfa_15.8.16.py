from functools import reduce


def evaluate(coefficients, x):
    return reduce(lambda j, k: j + k, map(lambda i: i[0]*x**(len(coefficients) - i[1]), coefficients))


if __name__ == '__main__':
    print(evaluate([(int(m), n) for n, m in enumerate(input().split(), 1)], int(input())))
