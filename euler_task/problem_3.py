"""Задача Эйлера №3:
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""

import time

start = time.time()

y = 600851475143
i = 2
list_1 = []

while i < y ** 0.5:
    if y % i == 0 and (2 ** i - 2) % i == 0:
        list_1 += [i]
        if y % i == 0 and (2 ** (y // i) - 2) % (y // i) == 0:
            list_1 += [y // i]
    i += 1

result = list_1[-1]

print(result)

end = time.time()
print('Время выполнения: {:.2f} сек. (~ {:.1f} мин.)'.format((end - start), ((end - start) / 60)))
