from turtle import Turtle, Screen
import random

timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")

colors = [
    "sea green",
    "yellow",
    "dodger blue",
    "medium spring green",
    "royal blue",
    "dark gray",
    "cornflower blue",
    "crimson",
    "salmon",
    "tomato",
    "pale violet red",
    "dark magenta",
    "maroon",
    "gold",
]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for i in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(i)


my_screen.exitonclick()
