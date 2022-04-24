from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(100)


def move_backward():
    tim.backward(100)


def rotate_clockwise():
    angle = tim.heading()
    tim.setheading(angle + 5)


def rotate_anticlockwise():
    angle = tim.heading()
    tim.setheading(angle - 5)


def clear_screen():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_anticlockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
