import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = turtle.textinput(title="epic turtle race", prompt="who do you think is gonna win the race (COLOR)").lower()
print(user_bet)
#list of the colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-80, -50, -20, 10, 40, 70]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"you very correct!!! yay! {winning_color} win!!!")
            else:
                print(f"you were not correct. {winning_color} won.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()