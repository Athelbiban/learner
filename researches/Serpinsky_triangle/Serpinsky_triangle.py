import turtle as trl
import random as rnd
import math
import time

start = time.time()

trl.speed(0)
trl.Screen().bgcolor('black')
trl.Screen().screensize(700, 700)
trl.color('red')
trl.penup()

point = 100
R = 200
colour = 'yellow'
point_size = 2
size = 2*R*math.sin(math.radians(180/3))
trl.goto(0, -150)
trl.dot(point_size, colour)
lst = [(0, -150)]

for i in [60, 120]:
    trl.lt(i)
    trl.fd(size)
    trl.dot(point_size, colour)
    lst.append(trl.pos())

trl.goto(rnd.randint(-350, 350), rnd.randint(-350, 350))

for e in range(point):
    coord = rnd.choice(lst)
    trl.setheading(trl.towards(coord))
    trl.fd(trl.distance(coord) / 2)
    trl.dot(point_size, colour)

print(time.time() - start)
trl.done()
