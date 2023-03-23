from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
#canvas.create_line(0,0, 500,500, fill='blue', width=3)
#canvas.create_line(0,500, 500,0, fill='red', width=3)
#canvas.create_rectangle(25,25, 250,250, width=3, fill='purple')
#canvas.create_polygon(250,0, 500,500, 0,500, fill='yellow', outline='black', width=2)
#canvas.create_polygon(0,250, 0,500, 500,500)
#canvas.create_arc(0,0, 500,500, fill='red', style=PIESLICE, extent=180, width=2)

# POKEBALL DESIGN

canvas.create_arc(0,0, 500,500, fill='red', extent=180, width=5)
canvas.create_arc(0,0, 500,500, fill='white', start=180, extent=180, width=5)
canvas.create_oval(190,190, 310,310, fill='white', width=5)


canvas.pack()

window.mainloop()