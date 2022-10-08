import turtle as t
import random as r
import math as m


def get_square(radius, color):
    side = 2*radius * m.sin(m.radians(2*180/4))
    t.fd(side / 1.5)
    t.lt(45)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius * 2, 360, 4)
    t.end_fill()
    t.rt(45)
    t.bk(side / 1.5)
    pass


def get_hexagon(radius, color):
    side = 2*radius * m.sin(m.radians(2*180/6))
    t.penup()
    t.fd(side * 1.1)
    t.lt(90)
    t.fd(side)
    t.rt(90)
    t.lt(90)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius * 2, 360, 6)
    t.end_fill()
    t.rt(90)
    t.penup()
    t.bk(side * 1.1)
    t.lt(90)
    t.bk(side)
    t.rt(90)
    t.pendown()
    pass


def get_polygon(radius, sides, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius * 2, 360, sides)
    t.end_fill()
    pass


y = [200, 100, 0, -100, -200]
S = 800
t.speed(0)
t.hideturtle()

for i in range(5):
    for e in range(4, -1, -1):
        t.penup()
        t.goto(y[e], y[i])
        t.pendown()
        n = r.randint(3, 7)
        R = m.sqrt(2*S / (n * m.sin(m.radians(2*180/n))))
        t.colormode(255)
        c = r.randrange(256), r.randrange(256), r.randrange(256)
        if n == 4:
            get_square(R, c)
        elif n == 6:
            get_hexagon(R, c)
        else:
            get_polygon(R, n, c)

t.done()
