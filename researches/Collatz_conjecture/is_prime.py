def sum_prime(num):
    lst = list(range(num + 1))
    for i in range(2, int(num ** 0.5) + 1):
        if lst[i]:
            for e in range(i * i, num + 1, i):
                lst[e] = 0
    return True if num in lst else False


if __name__ == '__main__':
    print(sum_prime(97))
