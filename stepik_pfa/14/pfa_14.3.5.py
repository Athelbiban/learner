import turtle as t

t.speed(0)
t.hideturtle()
lst = ['#FF2600', '#FFAA00', '#D4FA00', '#31FA00', '#00FA79',
       '#00FDFF', '#0080FF', '#4434FF', '#D83CFF', '#FF32A9']
for i in range(10):
    t.penup()
    t.goto(0, -200)
    t.goto(0, -200 + 20*i)
    t.pendown()
    t.fillcolor(lst[i])
    t.begin_fill()
    t.circle(200 - 20*i)
    t.end_fill()
t.done()
