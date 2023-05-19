from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

ball = Turtle()
ball.color("white")
ball.shape("square")

screen.exitonclick()