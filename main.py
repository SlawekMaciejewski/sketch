from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
screen.title("SKETCH in Python")


def draw_ff():
    pen.forward(10)


def draw_back():
    pen.backward(10)


def clear():
    pen.reset()


def rotate_counter_clockwise():
    pen.left(5)


def rotate_clockwise():
    pen.right(5)


screen.listen()
screen.onkeypress(key="w", fun=draw_ff)
screen.onkeypress(key="s", fun=draw_back)
screen.onkeypress(key="a", fun=rotate_counter_clockwise)
screen.onkeypress(key="d", fun=rotate_clockwise)
screen.onkeyrelease(key="c", fun=clear)

screen.exitonclick()
