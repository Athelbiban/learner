lst = ["камень", "ножницы", "бумага"]
t, r = lst.index(input()), lst.index(input())

if abs(t - r) == 1:
    print("Тимур" if t < r else "Руслан")
elif abs(t - r) > 1:
    print("Тимур" if t > r else "Руслан")
else:
    print("ничья")
