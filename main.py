from turtle import Screen, Turtle
from typing import Sequence
from paddle import Paddle
from ball import Ball
from time import sleep
#setting up screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("KQari's Pong")


#setting up paddles
screen.tracer(0)
paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))

#setting up ball
ball = Ball()


#making paddle movable
screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")

sleep_time = 0.03
start = True
while start == True :
    sleep(sleep_time)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(paddle_r.position()) < 50 and ball.xcor() >320 or ball.distance(paddle_l.position()) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if sleep_time > 0.002:
            sleep_time -= 0.002  
        print(sleep_time)

    
    if ball.xcor() > 400:
        print("left guy scored")
        ball.goto(0,0)
        ball.bounce_x()
        sleep_time = 0.03

    if ball.xcor() < -400:
        print("right guy scored")
        ball.goto(0,0)
        ball.bounce_x()
        sleep_time = 0.03



screen.exitonclick()
