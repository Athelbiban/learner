import turtle as t

t.speed(5)
t.pensize(2)
t.pencolor('lightseagreen')
for i in range(10):
    t.goto(135 - i*30, -150)
    t.dot(5, 'blue')
    t.penup()
    t.goto(0, 0)
    t.pendown()
t.dot(7, 'orange')
t.hideturtle()
t.done()
