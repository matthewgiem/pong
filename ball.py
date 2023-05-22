from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.shape("circle")
        self.start_game()

    def start_game(self):
        self.setheading(random.randint(0, 100) - 50)

    def inplay(self, speed):
        self.forward(speed)

    def bounce_roof(self):
        heading = self.heading()
        if 0 < heading < 90:
            self.setheading(heading - 90)
        if 90 < heading < 180:
            self.setheading(heading + 90)
        if 180 < heading < 270:
            self.setheading(heading - 90)
        if 270 < heading < 360:
            self.setheading(heading + 90)
