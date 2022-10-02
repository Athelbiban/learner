import turtle as t

t.shape('turtle')
t.Screen().bgcolor('darkseagreen')
t.penup()
for i in range(5, 42):
    t.rt(22)
    t.fd(i)
    t.stamp()
