import turtle as t

t.shape('turtle')
t.stamp()
t.Screen().bgcolor('powderblue')
t.pensize(4)
for _ in range(12):
    t.penup()
    t.fd(70)
    t.pendown()
    t.fd(15)
    t.penup()
    t.fd(15)
    t.stamp()
    t.bk(100)
    t.lt(30)
