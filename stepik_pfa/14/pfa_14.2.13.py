import turtle as t

t.speed(5)
t.pensize(6)
lst = [0, 0, 0, -70, -70]
lst1 = ['red', 'black', 'blue', 'yellow']
t.pencolor('green')
t.penup()
t.goto(0, -70)
t.pendown()
t.circle(50)
for i in range(3):
    t.penup()
    t.goto(50 - 106*i, 0)
    t.pencolor(lst1[i])
    t.pendown()
    t.circle(50)
t.penup()
t.goto(-106, -70)
t.pencolor(lst1[3])
t.pendown()
t.circle(50)

t.done()
