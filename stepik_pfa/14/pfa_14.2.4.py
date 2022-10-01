import turtle as t
import math

numbers_web_ray = 8  # Число лучей паутины кратное 360
web_rings = 5
length_ray = 200
ind = length_ray // (web_rings + 1)
a = 90 / (numbers_web_ray / 4)
b = (180 - a) / 2
c = 180 - b

t.dot(10)
for j in range(0, 360, 360 // numbers_web_ray):
    t.setheading(j)
    t.fd(length_ray)
    t.stamp()
    t.lt(180)
    t.fd(length_ray)

for i in range(1, web_rings + 1):
    t.setheading(0)
    t.fd(ind)
    t.lt(c)
    for _ in range(numbers_web_ray):
        t.fd(math.sqrt(2*(ind*i)**2 - 2*(ind*i)**2*math.cos(a/360*math.pi*2)))
        t.lt(a)
