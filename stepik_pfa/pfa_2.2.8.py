s = ["ножницы", "бумага", "камень", "ящерица", "Спок"]
d = ["ножницы", "ящерица", "бумага", "Спок", "камень"]
t, r = input(), input()
t1, r1 = s.index(t), s.index(r)
t2, r2 = d.index(t), d.index(r)

if abs(t1 - r1) == 1 or abs(t2 - r2) == 1:
    if t1 < r1:
        print("Тимур")
    elif t2 < r2:
        print("Тимур")
    else:
        print("Руслан")
elif abs(t1 - r1) == 4 or abs(t2 - r2) == 4:
    if t1 > r1:
        print("Тимур")
    elif t2 > r2:
        print("Тимур")
    else:
        print("Руслан")

else:
    print("ничья")
