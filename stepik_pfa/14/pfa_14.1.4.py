import turtle as t


def square(side):
    lst = [15, 45, 75]
    for i in lst:
        t.setheading(i)
        t.fd(side)
        t.lt(90)
        t.fd(side)
        t.lt(90)
        t.fd(side)
        t.lt(90)
        t.fd(side)


if __name__ == '__main__':
    square(int(input()))
