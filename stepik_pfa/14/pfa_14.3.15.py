import turtle as tl
import numpy as np
import math as m

tl.speed(0)
tl.pencolor('red')
tl.fillcolor('red')
tl.begin_fill()

for t in np.arange(0, 6.3 + 0.01, 0.01):
    x = 128 * m.sin(t)**3
    y = 8*(13*m.cos(t) - 5*m.cos(2*t) - 2*m.cos(3*t) - m.cos(4*t) - 5)
    tl.goto(x, y)

tl.end_fill()
tl.done()
