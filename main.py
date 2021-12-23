from turtle import Screen, Turtle
import turtle
from typing import Sequence

#setting up screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("KQari's Pong")


#setting up paddle
paddle = Turtle()
screen.tracer(0)
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(350,0)
paddle.shape("square")

#making paddle movable
def move_up():
    paddle.goto(paddle.xcor(), paddle.ycor()+20)
def move_down():
    paddle.goto(paddle.xcor(), paddle.ycor()-20)

    
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")


start = True
while start == True :
    screen.update()
   



screen.exitonclick()
