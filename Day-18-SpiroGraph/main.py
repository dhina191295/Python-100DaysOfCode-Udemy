import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim = t.Turtle()
tim.shape('arrow')
tim.speed("fastest")
t.colormode(255)

angle = 0
cond = True

while cond:
    color = random_color()
    tim.color(color)
    tim.pencolor(color)
    tim.circle(100)
    tim.setheading(angle)
    angle += 5
    if angle > 360:
        cond = False

screen = t.Screen()
screen.exitonclick()
