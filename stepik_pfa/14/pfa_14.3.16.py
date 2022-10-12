import turtle as t
import random as r


def paint_star(x, y):
    t.penup()
    t.goto(x, y)
    t.lt(r.randrange(361))
    c = (r.randrange(256), r.randrange(256), r.randrange(256))
    t.pencolor(c)
    t.fillcolor(c)
    t.pendown()
    k = r.randint(2, 10)
    t.begin_fill()
    for i in range(5):
        t.circle(k, 280, 2)
        t.lt(150)
    t.end_fill()


def main():
    t.Screen().setup(720, 720)
    t.bgcolor('black')
    t.colormode(255)
    t.speed(0)
    t.Screen().onclick(paint_star)

    t.done()


if __name__ == '__main__':
    main()
