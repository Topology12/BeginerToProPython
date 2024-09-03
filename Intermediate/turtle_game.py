import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(500, 500)

screen.listen()


# def move_forwards():
# #     my_turtle.forward(50)
# #
# #
# # screen.onkey(move_forwards, "a")

# def move_forwards():
#     my_turtle.forward(50)


# def move_backwards():
#     my_turtle.backward(50)
#
#
# def turn_left():
#     new_heading = my_turtle.heading() + 10
#     my_turtle.setheading(new_heading)
#
#
# def turn_right():
#     new_heading = my_turtle.heading() - 10
#     my_turtle.setheading(new_heading)
#
#
# def clear():
#     my_turtle.clear()
#     my_turtle.penup()
#     my_turtle.home()
#     my_turtle.pendown()
#
#
# screen.onkey(clear, key="space")
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.exitonclick()

colors = ['red', 'green', 'blue', "yellow", "purple", 'orange']
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
lst_turtles = []
position = [(-250, -150), (-250, -90), (-250, -30), (-250, 30), (-250, 90), (-250, 150)]


def turtle_move_left_wall(turtle, position):
    turtle.goto(position[0], position[1])


for i in range(6):
    new_turtle = Turtle()
    new_turtle.color(colors[i], colors[i])
    new_turtle.shape("turtle")
    new_turtle.penup()
    lst_turtles.append(new_turtle)
    turtle_move_left_wall(new_turtle, position[i])

is_race_on = False
if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in lst_turtles:
        if turtle.xcor() > 220:
            if turtle.pencolor() == user_choice:
                print(f"You 've won! The {turtle.pencolor()} turtle is winning!")
            else:
                print(f"You 've lost! The {turtle.pencolor()} turtle is winning!")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
