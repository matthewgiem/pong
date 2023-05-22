from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.shape("circle")
        self.start_game()
        self.speed = speed

    def start_game(self):
        self.setheading(random.randint(0, 100) - 50)

    def inplay(self):
        self.forward(self.speed)

    def bounce_roof(self):
        self.setheading(-self.heading())

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
