import turtle


def triangle(side):
    turtle.forward(side)
    turtle.setheading(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)


if __name__ == '__main__':
    triangle(int(input()))
