from tkinter import *

window = Tk()
window.title("cool gui")
window.minsize(width=500, height=300)

'''Label'''
my_label = Label(text="hi", font=("Jost", 24, "italic"))
my_label.pack()

my_label["text"] = "hello world"
my_label.config(text="hello world")

def button_clicked():
    print("haha you got scammed no million dollars!!!")
    my_label.config(text="haha you got scammed no million dollars!!!")
    button.config(text="scammed haha")

button = Button(text="click for 1 million dollars", command=button_clicked)
button.pack()

def name_print():
    name = input.get()
    print(name)

input = Entry()
input.pack()
input_button = Button(text="click to print name in console", command=name_print)
input_button.pack()




window.mainloop()
