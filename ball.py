from time import sleep
from turtle import Turtle 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto((0,0))
        self.shape('circle')
        self.x = 10
        self.y = 10

    def move_ball(self):
        self.goto(self.xcor()+self.x, self.ycor()+self.y)


    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
    


