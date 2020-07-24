from tkinter import *

def update():
    print("Updating the GUI")
    root.geometry(f"{width.get()}x{width.get()}")

root = Tk()
root.geometry("644x245")
root.title("GUI")
width=StringVar()
height=StringVar()
Entry(root, textvariable=width).pack()
Entry(root, textvariable=height).pack()
Button(root, text="Apply", command=update).pack()
root.mainloop()