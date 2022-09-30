import turtle as t

side1 = 100
side2 = 110

for i in range(10, 360 + 1, 36):
    t.setheading(i)
    for j in [0, 120]:
        t.lt(j)
        t.fd(side1)
        t.lt(60)
        t.fd(side2)
