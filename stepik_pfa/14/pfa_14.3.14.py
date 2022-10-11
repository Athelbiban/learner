import turtle as t
import random as r
import numpy as np


def paint_buildings():
    t.penup()
    t.goto(-350, -100)
    t.pendown()
    t.pencolor('blue')
    t.fillcolor('blue')
    t.begin_fill()
    t.fd(100)
    t.lt(90)
    t.fd(150)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.fd(150)
    t.rt(90)
    t.fd(250)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(180)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(120)
    t.lt(90)
    t.fd(50)
    t.rt(90)
    t.fd(150)
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(260)
    t.rt(90)
    t.fd(700)
    t.rt(90)
    t.fd(250)
    t.end_fill()


def paint_windows():
    t.shape('square')
    t.shapesize(1)
    t.color('yellow')
    t.penup()
    t.goto(-120, 220)
    t.stamp()
    t.goto(-120, 190)
    t.stamp()
    t.goto(-35, 120)
    t.stamp()
    t.goto(120, 100)
    t.stamp()
    t.goto(-220, 10)
    t.stamp()
    t.goto(-80, -120)
    t.stamp()


def paint_stars():
    t.penup()
    t.shape('circle')
    t.color('yellow')
    for i in range(300):
        R = r.choice(np.arange(0.01, 0.15, .01))
        x, y = (r.randint(-350, 350) for _ in '..')
        t.turtlesize(R)
        t.goto(x, y)
        t.stamp()


def main():
    t.Screen().setup(700, 700)
    t.speed(0)
    t.bgcolor('darkblue')
    paint_stars()
    paint_buildings()
    paint_windows()
    t.ht()
    t.done()
    pass


if __name__ == '__main__':
    main()
