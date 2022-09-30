import turtle as t


def square(side):
    for i in range(0, 320, 45):
        t.setheading(i)
        for _ in '1234':
            t.fd(side)
            t.lt(90)


if __name__ == '__main__':
    square(int(input()))
