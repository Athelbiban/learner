def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif 2 < x:
        return (x - 2) ** 2 + 1
    else:
        return -x / 2


print(f(float(input())))
