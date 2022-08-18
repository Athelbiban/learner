"""Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом?"""

import time

start = time.time()

index = 0
n = 1
a = 10001
while index < a:
    n += 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        index += 1
print(n)

end = time.time()
print('Время выполнения: {:.2f} сек. (~ {:.1f} мин.)'.format((end - start), ((end - start) / 60)))
