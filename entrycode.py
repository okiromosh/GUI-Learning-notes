from tkinter import *

window = Tk()


def submit():
    username = entry.get()
    print(f"Hello {username}")


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


entry = Entry(window,
              font=("", 20)
              )
entry.pack(side=LEFT)

submit_button = Button(window, text="Submit", command=submit, )
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete, )
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace, )
backspace_button.pack(side=RIGHT)

window.mainloop()
