from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1
        '''initializes attributes and inherits turtle using superclass like scoreboard'''

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        '''ball moves by adding the x coordinate and y coordinate + 3 because the x_move
            and y_move are 3'''

    def bounce_y(self):
        self.y_move *= -1
        '''bounce_y used for when ball hits the surface of the y axis'''

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        '''bounce_x used for when ball hits the surface of the x axis'''

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
        '''resets position once either paddle scores a point'''

