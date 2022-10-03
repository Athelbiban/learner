import turtle as t

t.speed(2)
t.lt(60)
for i in '..':
    t.fd(100)
    t.lt(120)
t.fd(100)
t.penup()
t.goto(0, 115)
t.pendown()
for _ in '..':
    t.fd(100)
    t.rt(120)
t.fd(100)

t.done()
