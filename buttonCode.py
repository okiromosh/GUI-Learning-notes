from tkinter import *

window = Tk()

count = 0

def click():
    global count
    count += 1
    print(f"You have clicked {count} times")


button = Button(window,
                text="Click Me",
                command=click,
                state=ACTIVE,
                fg="black"


                )
button.pack()

window.mainloop()
