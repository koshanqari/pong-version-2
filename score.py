from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score_l = 0
        self.score_r = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=('Arial', 60, 'normal'))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=('Arial', 60, 'normal'))

    def update_l(self):
        self.score_l +=1
        

    def update_r(self):
        self.score_r +=1
        

    

    
