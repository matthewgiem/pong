from turtle import Turtle
# add pass through to change which paddle we are refrencing


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if side == "right":
            self.goto(380, 0)
        if side == "left":
            self.goto(-380, 0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 10)