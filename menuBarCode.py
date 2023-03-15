from tkinter import *


def openFile():
    print("Opening File")


def saveFile():
    print("Saving File")


def cut():
    print("Cut")


def copy():
    print("Copy")


def paste():
    print("Paste")


window = Tk()

menuBar = Menu()
window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0, )
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(labe='Open', command=openFile)
fileMenu.add_command(label='Save', command=saveFile)
fileMenu.add_separator()  # adds a separator between commands
fileMenu.add_command(label='Exit', command=quit)

editMenu = Menu(menuBar, tearoff=0, )
menuBar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)

window.mainloop()
