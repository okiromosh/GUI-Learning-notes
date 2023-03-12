from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    # print(color)
    colorHex = color[1]  # chooses output to index [1]
    # print(colorHex)
    window.config(bg=colorHex)
    # window.config(colorchooser.askcolor()[1])     all the code in one line


window = Tk()

window.geometry('400x400')

button = Button(window, text="Click Me", command=click)
button.pack()

window.mainloop()
