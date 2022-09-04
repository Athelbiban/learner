s = ["ножницы", "бумага", "камень", "ящерица", "Спок"]
d = ["ножницы", "ящерица", "бумага", "Спок", "камень"]
t, r = input(), input()
t1, r1 = s.index(t), s.index(r)
t2, r2 = d.index(t), d.index(r)
abs1, abs2 = abs(t1 - r1), abs(t2 - r2)

if abs1 == 1 or abs2 == 1:
    if t1 < r1 and abs1 == 1:
        print("Тимур")
    elif t2 < r2 and abs2 == 1:
        print("Тимур")
    else:
        print("Руслан")
elif abs1 == 4 or abs2 == 4:
    if t1 > r1 and abs1 == 4:
        print("Тимур")
    elif t2 > r2 and abs2 == 4:
        print("Тимур")
    else:
        print("Руслан")
else:
    print("ничья")
