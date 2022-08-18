a, b = int(input()), int(input())
counter = 0
summ = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        summ += i
        counter += 1
print(summ / counter)
