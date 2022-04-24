
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")

for i in range(15):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)

screen = Screen()

screen.exitonclick()
