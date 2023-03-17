from tkinter import *


def create_window():
    # new_window = Toplevel()     # create a new window on top of a bottom window. closes if bottom is closed
    new_window = Tk()           # create an independent new window

    # old_window.destroy()          closes out the previous/old window


old_window = Tk()

Button(old_window, text="create new window", command=create_window).pack()

old_window.mainloop()