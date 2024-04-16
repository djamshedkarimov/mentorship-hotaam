import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
'''import the modules'''

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
'''setup the screen'''

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
'''object for the classes in the different modules'''

screen.listen()
screen.onkey(player.go_up, "Up")
'''listents to the keystroke of the up arrow'''

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    '''updates screen every 0.1 second'''

    car_manager.create_car()
    car_manager.move_cars()
    '''moves cars and creates car for the game'''



    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            '''if you collide with a car, game over'''

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        '''if you cross the road without getting hit by a car,
            the level increases and the speed increments by 10
            you also go back to where you started'''





screen.exitonclick()
