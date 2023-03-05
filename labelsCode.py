from tkinter import *

window = Tk()
window.geometry("320x420")
window.title("GUI Window")

photo = PhotoImage(file='icon.png')

label = Label(window,
              text="This is a label that hold text/image in a window",
              font=('Arial'),
              fg='green',
              bg='white',
              relief=RAISED,
              bd=2,
              padx=10,
              image=photo, compound='bottom'
              )
label.pack()
# label.place()

window.mainloop()