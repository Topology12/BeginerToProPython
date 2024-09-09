from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.lets_start()

    def go_up(self):
        self.forward(10)

    def lets_start(self):
        self.goto(0, -280)