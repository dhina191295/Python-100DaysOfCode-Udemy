import random
import turtle as t

tim = t.Turtle()
color = ['black', 'chartreuse', 'red', 'green', 'magenta', 'yellow', 'cyan']

for i in range(3, 11, 1):
    angle = 360 / i
    t.pencolor(random.choice(color))
    for _ in range(i):
        t.pendown()
        t.forward(100)
        t.right(angle)
        t.forward(100)

screen = t.Screen()
screen.exitonclick()
