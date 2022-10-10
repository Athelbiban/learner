import turtle as t

t.Screen().setup(1300, 600)
t.speed(1)
R = [3, 4, 3, 2]
t.shape('circle')
t.penup()
t.goto(-400, 0)
t.shapesize(10)
t.stamp()
for i in range(3):
    t.shapesize(R[i])
    t.color('red')
    t.stamp()
    t.fd(R[i] * 30)



# for i in range(5):
#     r = -300 + R[i]*3
#     t.goto(r, -R[i])
#     print(-300 + 50*i, -R[i])
#     t.circle(R[i])

t.done()
