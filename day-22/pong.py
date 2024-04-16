from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
'''importing the modules'''

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
'''setting up the screen'''

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
'''objects from classes'''

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
'''press key and the function will happen'''

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    '''updates screen and ball moves while the game is on'''

    '''detects collision with ball and wall'''
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    '''detect collision with paddle and ball'''
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    '''detect if right paddle misses'''
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        '''left paddle gets point and resets the ball's position to continue the game'''

    '''detect if left paddle misses ball'''
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        '''right paddle gets point and ball resets position to continue game'''

screen.exitonclick()
