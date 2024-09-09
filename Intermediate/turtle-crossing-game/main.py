import time
from turtle import Turtle, Screen
from car import Car
from player import Player
from score_board import ScoreBoard

screen = Screen()
screen.setup(600, 600)
player = Player()
car_manager = Car()
score_board = ScoreBoard()
screen.tracer(0)
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()
    if player.ycor() > 250:
        player.lets_start()
        car_manager.update_speed()
        score_board.update_level()

screen.exitonclick()
