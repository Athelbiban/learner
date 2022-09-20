d = {}

for _ in range(int(input())):
    k, v = input().split(':')
    d[k.lower()] = v.lstrip()

for _ in range(int(input())):
    key = input().lower()
    print(d[key] if key in d else 'Не найдено')
