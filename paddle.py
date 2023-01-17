from turtle import Turtle

UPPER_POSITION = 230
LOWER_POSITION = -220
STEP = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.color("white")
        self.penup()
        self.set_position(position)
    
    def set_position(self, position):
        self.setposition(position)
    
    def up(self):
        current_x = self.xcor()
        current_y = self.ycor()
        
        if current_y < UPPER_POSITION:
            self.setposition(current_x, current_y + STEP)
            
    def down(self):
        current_x = self.xcor()
        current_y = self.ycor()
        
        if current_y > LOWER_POSITION:
            self.setposition(current_x, current_y - STEP)