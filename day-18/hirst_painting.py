import random
import turtle
#importing modules

# getting all information and setting up turtle for hirst painting
tim = turtle.Turtle()
tim.speed("fastest")
turtle.colormode(255)
color_list = [(248, 247, 244), (242, 250, 246), (250, 244, 248), (241, 244, 248), (5, 13, 37), (38, 21, 16), (130, 89, 57), (201, 140, 118), (234, 210, 85), (187, 138, 162), (213, 86, 69), (79, 8, 20), (38, 137, 63), (194, 80, 100), (145, 85, 104), (31, 87, 29), (74, 107, 139), (220, 177, 212), (25, 203, 173), (126, 160, 180), (152, 138, 63), (13, 71, 25), (10, 61, 136), (115, 186, 157), (123, 12, 31), (86, 133, 174), (21, 208, 218), (230, 175, 166), (240, 208, 6), (133, 223, 206), (103, 41, 33), (183, 189, 205), (75, 84, 32), (132, 217, 221), (6, 246, 217)]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_dots = 100

# for loop for printing the dots
for dot_count in range(1, num_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    # move forward and print dot and repeat

    # if number is like 90 or 80
    if dot_count % 10 == 0:
        # go to new line and continue printing dots
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle.Screen()
screen.exitonclick()