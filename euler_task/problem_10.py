import time

start = time.time()


def sum_prime(num):
    summ = 5
    for i in range(5, num, 2):
        for e in range(2, int(i ** 0.5) + 1):
            if not i % e:
                break
        else:
            summ += i
    end = time.time()
    return summ, 'Время выполнения: {:.5f} сек. (~ {:.1f} мин.)'.format((end - start), ((end - start) / 60))


if __name__ == '__main__':
    print(sum_prime(2_000_000))
