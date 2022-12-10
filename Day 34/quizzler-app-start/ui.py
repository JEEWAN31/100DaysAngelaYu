from tkinter import *
THEME_COLOR = "#375362"

class UserExperience:
    def __int__(self):
        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score_label = Label("text")
        self.ca = Canvas()
        self.ca.create_image()

        self.window.mainloop()