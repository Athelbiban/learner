import turtle as t

t.hideturtle()
t.speed(0)
t.Screen().bgcolor('#052DFE')
t.dot(200, '#FFAB00')
t.penup()
t.fd(200)
t.shape('circle')
t.shapesize(10)
t.color('#052DFE')
t.showturtle()

while True:
    for i in range(400):
        t.bk(1)
    # t.hideturtle()
    t.forward(400)
    # t.showturtle()
