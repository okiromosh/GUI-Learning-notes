from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="INFO BOX", message="This is an info message box")
    #messagebox.showwarning(title="WARNING BOX", message="This is a Warning Box")
    #messagebox.showerror(title="ERROR BOX", message="This is an Error Box")

    #if messagebox.askokcancel(title="ASK OK CANCEL", message="Do you want to do a thing"):
     #   print(":) You did the thing")
    #else:
      #  print(":( You canceled the thing")

    if messagebox.askretrycancel(title="ASK RETRY CANCEL", message="Do you want to retry a thing"):
        print("You retried")
    else:
        print("You canceled the retry")

window = Tk()

button = Button(window, text="click me", command=click)
button.pack()

window.mainloop()
