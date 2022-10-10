import turtle as t


lst = ['Восток', 'Запад', 'Север', 'Юг']
t.speed(0)
t.penup()
t.goto(0, -40)
t.pendown()
t.circle(40)
t.penup()
for i in [0, 90]:
    t.goto(0, 0)
    t.lt(i)
    t.pendown()
    t.fd(180)
    t.penup()
    t.fd(20)
    t.write(lst[i // 45], align=('center' if i // 45 == 'Север' or 'Юг' else 'right' if 'Восток' else 'left'),
            font=('Arial', 14, 'normal'))
    t.bk(20)
    t.pendown()
    t.bk(360)
    t.penup()
    t.bk(20)
    t.write(lst[i // 45 + 1], align=('center' if i // 45 == 'Север' or 'Юг' else 'right' if 'Восток' else 'left'),
            font=('Arial', 14, 'normal'))
t.rt(90)
t.done()
