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
        self.setheading(random.randint(0, 360))

    def inplay(self, speed):
        self.forward(speed)