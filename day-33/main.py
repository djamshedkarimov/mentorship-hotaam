from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)
    '''gets quote from api.kanye.rest'''


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
'''gui for kanye quote'''

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)
'''for image and text for the background image and text quote'''

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
'''the image of kanye'''



window.mainloop()
'''yay window doesnt exit immediately'''