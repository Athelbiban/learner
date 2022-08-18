import time

start = time.time()


def mountains_of_hoiyama(width):
    weight = width
    number_of_layers = width // 2 + 1
    for h in range(number_of_layers, width):
        weight_layer = h
        for w in range(width // 2, 0, -1):
            weight_layer += w * 2
        weight += weight_layer
    return weight


# def mountains_of_hoiyama(w):
#     return ((w + 1) ** 3 - w ** 2) // 8 + 1


# def mountains_of_hoiyama(width):
#     n = width // 2 + 1
#     return 2 * sum(2 * n ** 2 - 4 * n * i - 5 * n + 4 * i + 3 for i in range(n >> 1)) + n * (3 * n - 1) // 2


if __name__ == '__main__':
    print(mountains_of_hoiyama(10000001))

end = time.time()
print('Время выполнения: {:.2f} сек. (~ {:.1f} мин.)'.format((end - start), ((end - start) / 60)))
