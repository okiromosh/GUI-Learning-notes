from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 6
yVelocity = 7
window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT )
canvas.pack()

# background_img = PhotoImage(file="ar-sa.png")
# background = canvas.create_image(0,0, image=background_img, anchor=NW)

photo_img = PhotoImage(file="ar-sa.png")
my_img = canvas.create_image(0,0, image=photo_img, anchor=NW)

img_width = photo_img.width()
img_height = photo_img.height()


while True:
    coordinates = canvas.coords(my_img)
    print(coordinates)
    if coordinates[0] >= (WIDTH - img_width) or coordinates[0]<0:
        xVelocity = -xVelocity
    if coordinates[1] >= (HEIGHT - img_height) or coordinates[1]<0:
        yVelocity = -yVelocity
    canvas.move(my_img, xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()