from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
'''the variables for starting positions, distance, and the angles'''


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        '''initializes segments, creating the starting snake, and the head which is the first segment of the snake since the index is 0'''

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    '''for loop used to create the starting snake segments (3 segments since there are 3 positions in STARTING_POSITIONS
        also uses add_segment() to create the segments'''

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        '''function used to add segments. used in create_snake()'''

    def extend(self):
        self.add_segment(self.segments[-1].position())
        '''extends the snake by 1 by making another value in the segments list'''

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        '''moves the snake (start, stop, step)'''

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            '''moves up
                also checks if you are currently facing down'''

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            '''moves down
                also checks if you are currently facing up'''

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            '''moves left
                also checks if you are currently facing right'''

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            '''moves right
                also checks if you are currently facing left'''
