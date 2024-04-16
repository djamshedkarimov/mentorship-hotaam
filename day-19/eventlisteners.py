import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    tim.forward(10)

def right():
    tim.right(10)

def left():
    tim.right(-10)

def move_backward():
    tim.forward(-10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="c", fun=clear)



screen.exitonclick()