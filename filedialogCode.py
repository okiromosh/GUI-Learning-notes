        OPENING A FILE WITH FILEDIALOG

from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfile(title="Directory",
                                      filetypes=(("Text Files", "*.txt"),
                                                ("All Files","*.*")),

                                      )
    # print(filepath.name)
    file = open(filepath.name, "rt")
    print(file.read())
    file.close()




window = Tk()

button = Button(window, text="Open", command=openFile)
button.pack()

window.mainloop()

-------------------------------------------------------------------------------------
"""
            SAVING A FILE USING FILEDIALOG

from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initaldir="",
                                    defaultextension=".txt",
                                    filetypes=[("Text File", ".txt"),
                                               ("HTML File", ".html"),
                                               ("All Files", ".*")])
    if file is None:
        return  # stops the exception error

    filetext = str(text.get(1.0, END))
    # filetext = input("Enter some text: ")    Uses console input after saving the file
    file.write(filetext)
    file.close()


window = Tk()

text = Text(window)
text.pack()

button = Button(window, text="Save", command=saveFile)
button.pack()

window.mainloop()
"""
-------------------------------------------------------------------
