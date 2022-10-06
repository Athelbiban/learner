import turtle as t

t.Screen().bgcolor('#021B9D')
t.speed(0)
t.hideturtle()
t.penup()
t.pencolor('#021B9D')
lst = ['#FFB400', '#021B9D']
for i in range(2):
    t.goto(50 * i, -150)
    t.pendown()
    t.fillcolor(lst[i])
    t.begin_fill()
    t.circle(200)
    t.end_fill()
    t.penup()

t.done()
