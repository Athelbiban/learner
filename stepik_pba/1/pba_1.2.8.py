objects = [1, 2, 1, 2, 3, True, False, True, False, "true"]  # Для проверки

lst = []  # Решение 1
ans = 0
flag1 = None
flag2 = None

for obj in objects:
    if obj is True or obj is False:
        if obj is True and flag1 is None:
            ans += 1
            lst.append(obj)
            flag1 = True
        elif obj is False and flag2 is None:
            ans += 1
            lst.append(obj)
            flag2 = False
    elif obj not in lst:
        ans += 1
        lst.append(obj)

print(ans)


print(len({id(i) for i in objects}))  # Решение 2
