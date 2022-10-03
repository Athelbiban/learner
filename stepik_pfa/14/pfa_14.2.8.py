import turtle as t

c = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
for i in range(45):
    t.pencolor(c[i%6])
    t.pensize(i//3)
    t.fd(i*2)
    t.lt(45)
