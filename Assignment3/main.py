from tkinter import *

Background_color = "#FF9E9E"

screen = Tk()
screen.title("Tik-Tak-Toe")
screen.config(padx=10, pady=20, bg=Background_color)
canva = Canvas(width=500, height=500, bg="#FFCAC8", highlightthickness=0)
canva.pack()


screen.mainloop()
