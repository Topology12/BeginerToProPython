from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.position = pos
        self.paddle_position()

    def paddle_position(self):
        if self.position == 0:
            self.goto(-370, -0)
        else:
            self.goto(370, 0)

    def paddle_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def paddle_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_change = 10
        self.y_change = 10

    def move(self):
        new_x = self.xcor() + self.x_change
        new_y = self.ycor() + self.y_change
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_change *= -1

    def bounce_x(self):
        self.x_change *= -1

    def reset_ball(self):
        self.goto(0, 0)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 230)
        self.score_left = 0
        self.score_right = 0
        self.update_board()

    def write_score(self):
        self.write(f"{self.score_left} | {self.score_right}", align="center", font=("Arial", 50, "normal"))

    def left_score(self):
        self.score_left += 1

    def right_score(self):
        self.score_right += 1

    def update_board(self):
        self.clear()
        self.goto(0, 230)
        self.write_score()


score_board = ScoreBoard()
paddle_left = Paddle(0)
paddle_right = Paddle(1)
ball = Ball()
screen.listen()
screen.onkey(paddle_left.paddle_up, "Up")
screen.onkey(paddle_left.paddle_down, "Down")
screen.onkey(paddle_right.paddle_up, "w")
screen.onkey(paddle_right.paddle_down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle_right) < 50 and ball.xcor() > 360:
        ball.bounce_x()
    if ball.distance(paddle_left) < 50 and ball.xcor() < -360:
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.bounce_x()
        score_board.left_score()
        score_board.update_board()
        ball.reset_ball()
    if ball.xcor() < -390:
        score_board.right_score()
        score_board.update_board()
        ball.reset_ball()

screen.exitonclick()
