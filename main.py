from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")

screen.tracer(0)
paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")

screen.onkey(paddle2.go_up, 'w')
screen.onkey(paddle2.go_down, 's')

game_on = True

while game_on:
    time.sleep(0.02)
    screen.update()
    ball.move()

    # Making the ball bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Making the ball bounce once it hits the paddle
    if (ball.distance(paddle1)<50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_pos()
        score.paddle1_point()

        if score.paddle1_score == 10:
            game_on = False

    if ball.xcor() < -380:
        ball.reset_pos()
        score.paddle2_point()

        if score.paddle2_score == 10:
            game_on = False

screen.exitonclick()