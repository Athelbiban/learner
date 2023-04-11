import turtle


turtle.speed(0)  # максимальная скорость отрисовки
sw = 720  # ширина окна в пикселах
sh = sw // 2  # высота окна
turtle.setup(sw, sh)  # настройка размера окна
# turtle.up()  # поднимаем перо
# turtle.setpos(-sw // 2, -sh // 3)  # устанавливаем начальную позицию
# turtle.down()  # опускаем перо


def koch_turns(n, lst=[60, -120, 60]):
    if n > 0:
        return koch_turns(n-1)
    return


def turtle_koch_curve(n, line_length=10):
    for move in koch_turns(n):
        turtle.forward(line_length)
        turtle.left(move)
    turtle.forward(line_length)


turtle_koch_curve(2)
turtle.mainloop()
