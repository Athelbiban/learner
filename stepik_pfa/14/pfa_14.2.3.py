import turtle as t

dot = 20
line1 = 100
line2 = 200

for _ in '..':
    t.dot(dot)
    t.pencolor('skyblue4')
    t.fd(line2)
    t.pencolor('black')
    t.dot(dot)
    t.lt(90)
    t.pencolor('skyblue4')
    t.fd(line1)
    t.lt(90)
    t.pencolor('black')
