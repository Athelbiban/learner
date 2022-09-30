import turtle as t

n = 8
length = 200

t.dot(15)
for j in range(0, 360, 360 // n):
    t.setheading(j)
    t.fd(length)
    t.stamp()
    t.lt(180)
    t.fd(length)


