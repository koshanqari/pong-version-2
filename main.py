from turtle import Screen, Turtle
from typing import Sequence
from paddle import Paddle

#setting up screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("KQari's Pong")


#setting up paddles
screen.tracer(0)
paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))



#making paddle movable
screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")






start = True
while start == True :
    screen.update()
   



screen.exitonclick()
