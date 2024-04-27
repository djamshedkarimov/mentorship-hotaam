from tkinter import *
import math
'''importing math for math.floor and tkinter for gui'''
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
'''variables to help throughout pomodoro'''

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
    '''resets timer by:
        resetting the reps
        removing all the checkmarks
        changing the label back to Title
        resetting the timer'''


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    '''adds a rep every time you start a timer'''

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    '''the break seconds'''

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        '''if no remainder when reps divided by 8, foreground is red'''
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        '''if no remainder when reps divided by 2, foreground is pink'''
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        '''if just work, foreground is green'''

    count_down(5 * 60)
    '''minutes times the seconds in a minute'''


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    '''the minute and second for displaying timer in the tomato'''

    if count_sec == 0:
        count_sec = "00"
        '''if second is 0, it wont print "0", it will print "00"'''
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
        '''adds a 0 to the second since there is no tens place'''
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    '''prints the timer'''
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        '''update timer'''
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
        '''for every rep that is dvisible by 2, add checkmark'''


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
'''setting up window'''

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
'''label for timer, break, and work'''

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
'''the canvas for the tomato and the timer text'''


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
'''start button'''

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
'''reset button'''

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)
'''checkmarks'''









window.mainloop()