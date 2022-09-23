from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#  create as many paddles as you want at specified locations
user_paddle = Paddle((-350, 0))
comp_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(user_paddle.up, "w")
screen.onkey(user_paddle.down, "s")
screen.onkey(comp_paddle.up, "Up")
screen.onkey(comp_paddle.down, "Down")

scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with comp_paddle
    if ball.distance(comp_paddle) < 50 and ball.xcor() > 320 or ball.distance(user_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()
