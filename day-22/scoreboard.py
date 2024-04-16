from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        '''initializes the scoreboard attributes and inherits turtle using superclass'''

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        '''updates the scoreboard when either l_paddle or r_paddle gets a point'''

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        '''when left paddle scores, it goes to the update_scoreboard function'''

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        '''when right paddle scores, it goes to the update_scoreboard function'''
