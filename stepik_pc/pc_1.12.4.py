figure = input()

if figure == 'треугольник':
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif figure == 'прямоугольник':
    a, b = float(input()), float(input())
    print(a * b)
else:
    r = float(input())
    pi = 3.14
    s = pi * r ** 2
    print(s)
