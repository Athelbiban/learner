import time

start = time.time()


n = 2000000
list_number = [i for i in range(n+1)]
for i in range(2, int(n**.5)+1):
    if list_number[i]:
        for j in range(i*i, n+1, i):
            list_number[j] = 0
print(sum(list_number)-1)


end = time.time()
print('Время выполнения: {:.2f} сек. (~ {:.1f} мин.)'.format((end - start), ((end - start) / 60)))
