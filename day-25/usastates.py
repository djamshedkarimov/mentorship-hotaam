import turtle
import pandas
'''import turtle and pandas module
    turtle: for the image where the progress for naming all the states will be shown
    pandas: for importing csv easily and using additional methods to create the states game'''

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
'''setting up the screen and the image of the united states'''

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
'''the lists for the cvs and the guessed states'''

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    '''while there are less than 50 guessed states, get input set as answer_state'''
    if answer_state == "Exit":
        missing_states = []
        '''new list for missing states'''
        for state in all_states:
            '''for loop to check every item in all_states list from cvs'''
            if state not in guessed_states:
                '''check if state is not in guessed states'''
                missing_states.append(state)
                '''since the state has not yet been guessed, it is now in the missing_states list'''

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        '''if answer is not in guessed_states and is a correct state'''
        guessed_states.append(answer_state)
        '''adds state to the guessed_states'''
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        '''writes text of the name of state and puts it where the state is'''

