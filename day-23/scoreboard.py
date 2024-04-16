from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()
        '''inherits turtle to write scoreboard'''

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        '''updates the scoreboard every time it needs to be changed'''

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        '''increases the level every time you cross the road'''

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="left", font=FONT)
        '''writes game over in the middle of the screen if you lose'''
