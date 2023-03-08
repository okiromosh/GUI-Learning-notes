from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered PIZZA")
    elif x.get() == 1:
        print(" You ordered a HAMBURGER")
    elif x.get() == 2:
        print("You ordered a HOTDOG")
    else:
        print("Unknown")

window = Tk()

pizzaImage = PhotoImage(file="")
hamburgerImage = PhotoImage(file="")
hotdogImage = PhotoImage(file='')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]
x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[i],  # adds text from from food list to index number
                              variable=x,   # groups radiobutton together if they share the same variable
                              value=i,      # assigns each button a different value by index number
                              padx=20,      # adds padding to x-axis
                              pady=5,
                              font=("", 15),
                              image=foodImages[i],   # add images to buttons according to index
                              compound=LEFT,        # adds the image to the left side of text
                              indicatoron=0,         # removes the circle indicator
                              width=100,            # sets width of buttons
                              command=order
                              )
    radiobutton.pack(anchor=W               # anchors the buttons to the right side
                     )

window.mainloop()
