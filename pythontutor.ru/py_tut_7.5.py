"""
Задача «Больше своих соседей»
Условие
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите
количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""


s = [int(i) for i in input().split()]
count = 0
for i in range(1, len(s) - 1):
    if s[i - 1] < s[i] > s[i + 1]:
        count += 1
print(count)
