import turtle as trl
from math import sin, radians


def laser_coord(h, a, l):
    trl.speed(0)
    trl.goto(0, h)
    # trl.setheading(a)
    A = (1 - h) * sin(radians(90)) / sin(radians(a))
    C = A * sin(radians(a)) / sin(radians(90 - a))
    print(A, C)
    if l - A >= 0:
        trl.goto(C * 100, 1 * 100)

    return (0, 0)


if __name__ == '__main__':
    print(laser_coord(0.5, 60, 1.8))
    trl.done()
