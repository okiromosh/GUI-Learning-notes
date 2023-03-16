Frame =  a rectanguler container to group and hold widgets
--------------------------------------------------------------
from tkinter import *

window = Tk()

frame = Frame(window, bg="pink", bd=3, relief=SUNKEN)
frame.pack()

Button(frame, text="W", font=("Consolas",15), width=2).pack(side=TOP)
Button(frame, text="A", font=("Consolas",15), width=2).pack(side=LEFT)
Button(frame, text="S", font=("Consolas",15), width=2).pack(side=LEFT)
Button(frame, text="D", font=("Consolas",15), width=2).pack(side=LEFT)


window.mainloop()
