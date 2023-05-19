from turtle import Screen, Turtle
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle("right")
left_paddle = Paddle("left")
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# ball = Turtle()
# ball.color("white")
# ball.shape("square")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()