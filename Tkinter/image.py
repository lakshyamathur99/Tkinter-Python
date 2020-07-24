#image is a label
from tkinter import *
from PIL import Image, ImageTk
root=Tk()

root.geometry("955x944")

#image class
# for PNG 
photo = PhotoImage(file="charm.png")


#for jpg imaages
image = Image.open("charm.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(image=photo)
label.pack()

root.mainloop()

