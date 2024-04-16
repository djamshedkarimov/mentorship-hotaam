import turtle
import random

#from      turtle          import    Turtle
#keyword   module name     keyword   thing in module
# from turtle import * = import everything
# import turtle as t = alias
# just notes

# immutable - cannot be changed

# function to make a square
# def make_square(turtle):
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)

# initializing turtle as tim and setting speed
tim = turtle.Turtle()
tim.speed("fastest")

# for loop to make a dashed line using penup and pendown
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# make shapes with 3 to 10 sides
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

# directions = [0, 90, 180, 270]
# tim.pensize(15)
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# make random color RGB
#
#
# random walk using setheading and random color function
# for _ in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())


# make spirograph which is bunch of circles making another circle
def spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)
        tim.circle(100)
        
# spirograph(5)

# setting the screen where turtle is displayed as screen
screen = turtle.Screen()
screen.exitonclick()
# exit screen when you click
