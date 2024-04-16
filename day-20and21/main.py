from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
'''import libraries/modules from snake, food, and scoreboard'''

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
'''setting the screen (object) to:
    - black
    - titled to snake game
    - no pen
    - size is 600, 600
    '''

snake = Snake()
food = Food()
scoreboard = Scoreboard()
'''initializing objects from other modules'''

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
'''the screen.onkey method is used to listen if you press a key.
    Example: if i were to press the W key, the method would listen and do something when i press it
    the screen.listen is also used to listen to the keyboard'''

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    '''while loop is used to check if game is still running and screen.update() is used to update the screen
        time.sleep(0.1) is meant to pause the execution for 0.1 seconds since 0.1 is inputted
        after the pause, the snake object does a method
        '''

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        '''if statement used to refresh the food once you are within 15 pixels from the food.
            once it refreshes, it increases the scoreboard by 1 and adds another segment to the snake'''

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        '''this if statement is used to detect the collision with the borders.
            if you were to collide with the walls, then the game would be over.'''

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    '''this if statement is used to detect the collision with your other segments of the snake
        suppose you had a length of 10 segments and you accidentally hit one of them, then it would be game over'''





screen.exitonclick()
'''just used so the screen exits when you click and not immediately'''
