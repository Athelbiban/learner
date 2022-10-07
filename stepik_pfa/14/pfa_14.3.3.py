import turtle as t

t.hideturtle()
t.penup()
t.goto(-50, -180)
t.pendown()
t.rt(45)
for _ in range(2):
    t.begin_fill()
    t.circle(70, 90, 1)
    t.circle(160, 90, 1)
    t.end_fill()

t.lt(45)

lst1 = [20, 85, 150]
lst2 = ['green', 'yellow', 'red']
pos = t.pos()

for i in range(3):
    t.penup()
    t.goto(pos[0] + 50, pos[1] + lst1[i])
    t.pendown()
    t.fillcolor(lst2[i])
    t.begin_fill()
    t.circle(30)
    t.end_fill()

t.done()
