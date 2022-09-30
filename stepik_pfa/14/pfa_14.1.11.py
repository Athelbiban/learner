import turtle as t

side = 100

for i in range(36, 612 + 1, 144):
    t.setheading(i % 360)
    t.fd(side)
