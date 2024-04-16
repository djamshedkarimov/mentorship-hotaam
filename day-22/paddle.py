from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        '''initialize attributes and inherits turtle with superclass like ball and scoreboard'''

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        '''paddle moves up once you press a key in pong.py'''

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        '''paddle moves down once you press a key in pong.py'''

