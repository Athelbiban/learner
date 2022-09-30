import turtle as t

side = int(input())

for i in range(6):
    t.lt(60)
    t.fd(side)

for j in range(300, 600 + 1, 60):
    t.setheading(j % 360)
    for i in range(5):
        t.fd(side)
        t.lt(60)
