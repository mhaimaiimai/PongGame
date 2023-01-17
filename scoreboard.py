from turtle import Turtle

SCORE_LEFT_POSITION = (-200, 280)
SCORE_RIGHT_POSITION= (200, 280)
UPPER_POSITION = 270
LOWER_POSITION = -260
START_POSITION = (0,UPPER_POSITION)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score_left = 0
        self.score_right = 0
        self.display() 
    
    def display(self):
        self.clear()
        self.setposition(SCORE_LEFT_POSITION)
        self.write(f"Score: {self.score_left}", False, align="center", font=("Arial", 14, "normal"))
        self.setposition(SCORE_RIGHT_POSITION)
        self.write(f"Score: {self.score_right}", False, align="center", font=("Arial", 14, "normal"))
        
    def increase_score_l(self):
        self.score_left+=1   
        self.display() 
        
    def increase_score_r(self):
        self.score_right+=1   
        self.display() 
