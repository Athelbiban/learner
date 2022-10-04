import turtle as t
import random as r


def snowflake():
    size = r.randint(1, 6)
    t.pensize(size)
    t.Screen().colormode(255)
    clr = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
    t.pencolor(clr)
    n = r.randint(size*10, 70)
    t.dot()
    t.dot(n//10, clr)
    for _ in range(8):
        t.fd(n)
        for _ in range(3):
            t.bk(n/4)
            for u in [45, 270]:
                t.lt(u)
                t.fd(n/4)
                t.bk(n/4)
            t.lt(45)
        t.bk(n / 4)
        t.lt(45)
    pass


def main():
    t.Screen().title('Snowflakes')
    t.Screen().setup(700, 700)
    t.speed(0)
    t.bgcolor('cyan')
    lst = [(0, 0), (150, 150), (-150, -150), (-150, 150), (150, -150)]
    for i in range(5):
        t.penup()
        t.goto(lst[i])
        t.pendown()
        snowflake()
    t.done()


if __name__ == '__main__':
    main()
