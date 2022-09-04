a = ['Первая четверть:', 'Вторая четверть:',
     'Третья четверть:', 'Четвертая четверть:']
d = {i: 0 for i in a}

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > 0 < y:
        d[a[0]] += 1
    elif x < 0 < y:
        d[a[1]] += 1
    elif x < 0 > y:
        d[a[2]] += 1
    elif x > 0 > y:
        d[a[3]] += 1

for k, v in d.items():
    print(k, v)
