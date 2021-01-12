from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def draw_ff():
    pen.forward(10)


def draw_back():
    pen.backward(10)


screen.listen()
screen.onkeypress(key="w", fun=draw_ff)
screen.onkeypress(key="s", fun=draw_back)

screen.exitonclick()
