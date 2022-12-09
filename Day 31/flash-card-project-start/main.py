import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
df = pd.read_csv("data/french_words.csv")
dict1 = df.to_dict("record")
k = {}


def flip_card():
    Ca.itemconfig(Title, text="English", fill="white")
    Ca.itemconfig(Word, text=k["English"], fill="white")
    Ca.itemconfig(old_image, image=card_back)


def random_word():
    global k, flip_timer
    screen.after_cancel(flip_timer)
    k = random.choice(dict1)
    Ca.itemconfig(Word, text=k["French"])
    Ca.itemconfig(Title, text="French")
    Ca.itemconfig(old_image, image=card_front)
    flip_timer = screen.after(3000, func=flip_card)


screen = Tk()
screen.title("Flash Cards")
screen.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = screen.after(3000, func=flip_card)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

Ca = Canvas(width=800, height=526)
Ca.config(bg=BACKGROUND_COLOR, highlightthickness=0)
old_image = Ca.create_image(400, 263, image=card_front)
Word = Ca.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
Title = Ca.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
Ca.grid(row=0, column=0, columnspan=2)

# Ca.create_image()


galat = Button(image=wrong, highlightthickness=0, command=random_word)
galat.grid(row=1, column=0)
sahi = Button(image=right, highlightthickness=0, command=random_word)
sahi.grid(row=1, column=1)
random_word()

screen.mainloop()
