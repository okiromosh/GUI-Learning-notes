from tkinter import *

window = Tk()

titleLabel = Label(window, text="ENTER DETAILS", font=('', 10)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First Name: ", width=15, bg='light pink').grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text="Last Name: ", width=15, bg='light pink').grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text="Email Address: ", width=15, bg='green').grid(row=3, column=0)
emailNameEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()
