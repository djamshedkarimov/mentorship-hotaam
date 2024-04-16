from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        '''inherits turtle like scoreboard.py and sets up the turtle'''

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        '''goes up every time you press the up arrow key as said in main.py'''

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        '''goes to the start when you successfully cross the road'''

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        '''if cross road then it either returns true which will
            not break out of the while loop and opposite for when
            it returns false'''
