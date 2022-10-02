import turtle as t

n = 10
length = 100
t.shape('turtle')
t.stamp()
t.penup()
for i in range(0, 360, 360 // n):
    t.setheading(i)
    t.fd(length)
    t.stamp()
    t.lt(180)
    t.fd(length)
t.setheading(0)
