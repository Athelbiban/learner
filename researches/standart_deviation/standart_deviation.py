lst = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]

d = 0
avg_range = sum(lst) / len(lst)
for i in lst:
    e = (i - avg_range) ** 2
    d += e

sigma = (d / (len(lst) - 1)) ** 0.5
print(sigma)
