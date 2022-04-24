import random
import turtle as t


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_color():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    colors = (r, g, b)
    return colors


direction_values = [0, 90, 180, 270]

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()
tim.pensize(20)
tim.shape('arrow')
tim.speed(10)

cond = True
count = 0

while cond:
    # color = random.choice(colours)
    color = random_color()
    direction = random.choice(direction_values)
    tim.pencolor(color)
    tim.color(color)
    tim.setheading(direction)
    tim.forward(50)
    count += 1
    if count > 100:
        cond = False
