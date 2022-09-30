import turtle as t

side = 50

for _ in range(20):
    t.setheading(90)
    t.fd(side)
    for i in '123':
        t.lt(90)
        t.fd(side)
    side += 10
