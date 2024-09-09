from turtle import Turtle
import random

COLORS = ['red', 'green', 'blue', 'yellow', 'orange']


class Car:
    def __init__(self):
        self.all_cars = []
        self.speed = 10

    def create_car(self):
        random_change = random.randint(1, 6)
        if random_change == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-250, 250)
            new_car.goto(280, y_position)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def update_speed(self):
        self.speed += 10