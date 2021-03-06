from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.shape("square")
        

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+40)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-40)