from tkinter import *


def submit():
    print(f"The Temp is: {scale.get()} Degrees Celsius")


window = Tk()

hotImage = PhotoImage(file='icon.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100, to=0,
              length=300,
              font=('',10),
              tickinterval=10,
              troughcolor='#69EAFF'
              )
scale.pack()


button = Button(window, text="Submit", command=submit)
button.pack()
window.mainloop()
