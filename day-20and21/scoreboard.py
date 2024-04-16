from turtle import Turtle
from snake import Snake
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
'''font and alignment for scoreboard'''

snake = Snake()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        '''initializes scoreboard and uses superclass for inheritance'''

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        '''updates the scoreboard by rewriting the new current score'''

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        '''writes gameover once you lose'''

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        '''increases score every time you eat the food
            also goes to update_scoreboard() to print it'''
