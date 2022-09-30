import turtle as t


def hexagon(side):
    for i in range(0, 320, 60):
        t.setheading(i)
        for _ in '123456':
            t.fd(side)


if __name__ == '__main__':
    hexagon(int(input()))
