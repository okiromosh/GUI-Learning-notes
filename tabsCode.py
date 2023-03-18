from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window, )

tab1 = Frame(notebook, )
tab2 = Frame(notebook, )

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack(expand=True, fill="both")      # expand = will expand to fill an space otherwise not used
                                             # fill = fill space on both x and y axis

Label(tab1, text="This is tab#1", width=50, height=25).pack()
Label(tab2, text="This is tab#2", width=50, height=25).pack()


window.mainloop()