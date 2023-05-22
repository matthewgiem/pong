from turtle import Screen
from paddle import Paddle
from ball import Ball


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

score = 0
ball = Ball(0.125)
game_is_on = True
while game_is_on:
    screen.update()
    ball.inplay()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_roof()
    if ball.xcor() > 360 or ball.xcor() < -360:
        if ball.distance(right_paddle.pos()) < 60 or ball.distance(left_paddle.pos()) < 60:
            ball.speed = ball.speed * 1.1
            ball.bounce_paddle()
            score += 1
            print(f"the score of the game is {score}")

        else:
            print(f"the score of the game is {score}")
            game_is_on = False

screen.exitonclick()
