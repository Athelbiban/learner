import turtle as t
from math import sin, radians

t.ht()
t.speed(0)
t.pensize(2)
n = 4
R = 50
side = 2*R*sin(radians(180/n))
t.penup()

for i in range(5):
    t.goto(-(side*1.5), side*1.5 - side*i)
    for j in range(5):
        t.lt(45)
        t.pendown()
        t.fillcolor('white' if (i + j) % 2 else 'black')
        t.begin_fill()
        t.circle(R, 360, n)
        t.end_fill()
        t.penup()
        t.rt(45)
        t.fd(side)

t.done()
