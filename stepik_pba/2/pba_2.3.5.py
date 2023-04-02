import itertools


def primes():
    n = 1
    while True:
        n += 1
        for i in range(2, int(n**0.5) + 1):
            if not n % i:
                break
        else:
            yield n


print(list(itertools.takewhile(lambda x: x <= 11, primes())))
