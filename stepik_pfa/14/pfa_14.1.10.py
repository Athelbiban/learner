import turtle as t

side = 100

for i in range(0, 360, 30):
    t.setheading(i)
    t.fd(side)
    t.lt(180)
    t.fd(side)
