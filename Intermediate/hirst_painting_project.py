import random
import turtle
from turtle import Turtle, Screen
import colorgram



# for _ in range(4):
#   my_turtle.forward(100)
#   my_turtle.right(90)

#
# for i in range(15):
#     my_turtle.forward(10)
#     if i % 2 == 0:
#         my_turtle.penup()
#     else:
#         my_turtle.pendown()

# MAX = 360
# for i in range(3, 9):
#     for j in range(i):
#         my_turtle.forward(100)
#         my_turtle.right(MAX/i)
# colors = ["red", "green", "lightblue", "gray", "orange", "purple"]
# directions = [0, 90, 180, 270]
# for _ in range(50):
#     my_turtle.color(random.choice(colors))
#     my_turtle.forward(30)
#     my_turtle.setheading(random.choice(directions))

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# turtle.colormode(255)
#
# for _ in range(int(360/10)):
#     my_turtle.color(random_color())
#     my_turtle.circle(100)
#     my_turtle.setheading(my_turtle.heading() + 10)
# screen.turtles()
# screen.exitonclick()

# Project hirst painting
turtle.colormode(255)
my_turtle = Turtle()
rbg_colors = []
colors = colorgram.extract("images.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    current_color = (r, g, b)
    rbg_colors.append(current_color)


for i in range(10):
    for j in range(10):
        my_turtle.color(random.choice(rbg_colors))
        my_turtle.dot(20)
        my_turtle.penup()
        if j < 9:
            my_turtle.forward(40)
            my_turtle.pendown()
    my_turtle.penup()
    if i % 2 == 0:
        my_turtle.left(90)
        my_turtle.forward(60)
        my_turtle.left(90)
    else:
        my_turtle.right(90)
        my_turtle.forward(60)
        my_turtle.right(90)

