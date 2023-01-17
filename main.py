from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

LEFT_POSITION = (-370,0)
RIGHT_POSITION = (360,0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
UPPER_POSITION = 250
LOWER_POSITION = -260

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")

screen.tracer(0)
paddle_left = Paddle(LEFT_POSITION)
paddle_right = Paddle(RIGHT_POSITION)
scoreboard = ScoreBoard()
ball = Ball()

screen.listen()
screen.onkey(paddle_right.up,"Up")
screen.onkey(paddle_right.down,"Down")
screen.onkey(paddle_left.up,"w")
screen.onkey(paddle_left.down,"s")


is_game_on = True
while(is_game_on):
    time.sleep(ball.move_speed)
    screen.update()
    
    #bounce detection
    if (ball.ycor() >= UPPER_POSITION or 
        ball.ycor() <= LOWER_POSITION):
            ball.bounce_y()
    elif (ball.distance(paddle_right.pos()) < 50 and
          ball.xcor()>= RIGHT_POSITION[0]-20):
            ball.bounce_x()  
    elif (ball.distance(paddle_left.pos()) < 50 and
          ball.xcor()<= LEFT_POSITION[0]+20):
            ball.bounce_x() 
    elif (ball.xcor() >= SCREEN_WIDTH/2):
            scoreboard.increase_score_l()
            ball.reset_position()
    elif (ball.xcor() <= -1*SCREEN_WIDTH/2):
            scoreboard.increase_score_r()
            ball.reset_position()
    ball.move()

screen.exitonclick()