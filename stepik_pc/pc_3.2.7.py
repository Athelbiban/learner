def f(a): # Тестовая функция. Уже реализована в проверочном тесте.
    a *= a
    return a


d = {}
n = int(input())
counter = 0
while counter < n:
    x = int(input())
    if x not in d:
        d[x] = f(x)
    print(d[x])
    counter += 1

