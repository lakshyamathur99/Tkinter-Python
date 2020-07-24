from tkinter import *
root = Tk()
root.geometry("644x245")
root.title("ListBox")

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

i=0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of a listbox")

Button(root, text="Add item", command=add).pack()
root.mainloop()