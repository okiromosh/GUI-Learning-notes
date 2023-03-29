from tkinter import *


def doSomething(event):
    print(f"You clicked a button at {event.x},{event.y} ")


window = Tk()

window.bind("<Button-1>", doSomething)  # Mouse Left Click
# window.bind("<Button-2>", doSomething)      # Mouse Wheel Click
# window.bind("<Button-3>", doSomething)      # Mouse Right Click
# window.bind("<ButtonRelease>", doSomething)  # action on release of pressed button
# window.bind("<Enter>", doSomething)          # action the moment the cursor enters window
# window.bind("<Leave>", doSomething)          # action the moment the cursor leaves the window
# window.bind("<Motion>", doSomething)          # action as cursor moves around/inside the window


window.mainloop()
