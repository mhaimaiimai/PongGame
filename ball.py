from turtle import Turtle

STEP = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = STEP
        self.move_y = STEP
        self.move_speed = 0.08
    
    def move(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.setposition(current_x+self.move_x, current_y+self.move_y)
        
    def bounce_y(self):
        self.move_y *= -1 
        
    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9
        
    def reset_position(self):
        self.setposition(0,0)
        self.bounce_x()
        self.move_speed = 0.08
        