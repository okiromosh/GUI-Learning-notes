# Binds a function to a key from the keyboard

from tkinter import *

def doSomething(event):
    # print(f"You pressed {event.keysym}")
    label.config(text=event.keysym)



window = Tk()

window.bind("<Key>", doSomething)

label = Label(window, font=("",100))
label.pack()

window.mainloop()