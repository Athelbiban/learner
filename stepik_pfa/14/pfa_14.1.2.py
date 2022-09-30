import turtle


def rectangle(width, height):
    # turtle.showturtle()
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)


if __name__ == '__main__':
    rectangle(int(input()), int(input()))
