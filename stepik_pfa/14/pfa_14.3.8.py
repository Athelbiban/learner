import turtle as t
import random as r

# t.Screen().screensize(720, 720)
t.bgcolor('blue')
t.hideturtle()
t.speed(0)
t.tracer(25)
for e in range(300):
    t.penup()
    t.goto(r.randint(-500, 450), r.randint(-500, 450))
    t.lt(r.randrange(361))
    t.colormode(255)
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

t.done()
