from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.shape("circle")
        self.start_game(random.choice(["right", "left"]))
        self.speed = speed

    def start_game(self, side):
        if side == "right":
            self.setheading(random.randint(0, 100) - 50)
        elif side == "left":
            self.setheading(random.randint(180, 280) - 50)

    def inplay(self):
        self.forward(self.speed)

    def bounce_roof(self):
        self.setheading(-self.heading())

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
