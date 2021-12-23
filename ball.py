from time import sleep
from turtle import Turtle 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto((0,0))
        self.shape('circle')
        # self.setheading(45)

    def move_ball(self):
        
        # self.fd(10)
        self.goto(self.xcor()+10, self.ycor()+10)

