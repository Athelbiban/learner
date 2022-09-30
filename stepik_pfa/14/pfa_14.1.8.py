import turtle as t

side = int(input())

for i in [0, 180]:
    t.setheading(i)
    for j in [0, 120]:
        t.lt(j)
        t.fd(side)
