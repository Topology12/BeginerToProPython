from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-240, 250)
        self.update_board()

    def update_level(self):
        self.level += 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))