from tkinter import *
import requests as re


def get_quote():
    response = re.get(url='https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    print(quote)
    pass


get_quote()
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, )

window.mainloop()
# response = re.get(url="https://api.kanye.rest")
# print(response)
