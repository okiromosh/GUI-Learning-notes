from tkinter import *


def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("Your Order is:")
    # print(listbox.get(listbox.curselection())) works for selection one option at a time
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constasia", 15),
                  width=12,
                  selectmode=MULTIPLE,
                  )
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size())  # changes height depending on number of items in the list

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="SUBMIT", command=submit)
submitButton.pack()

addButton = Button(window, text="ADD", command=add)
addButton.pack()

window.mainloop()
