n = int(input())

if int(str(n)[-1]) == 0 or 5 <= int(str(n)[-2:]) <= 20 or 5 <= int(str(n)[-1]) <= 9:
    print(n, "программистов")
elif int(str(n)[-1]) == 1 and int(str(n)[-2:]) != 11:
    print(n, "программист")
else:
    print(n, "программиста")
