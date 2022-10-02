import turtle as t

for i in range(10, 21, 2):
    for e in ['red', 'blue', 'yellow', 'green', 'purple', 'orange']:
        t.pencolor(e)
        t.pensize(i // 2)
        t.fd(10*i)
        t.lt(45)
