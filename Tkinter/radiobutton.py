from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("644x344")
root.title("Radio Button")

def order():
    tmsg.showinfo("Order Received", f"We have received your order for {var.get()} , Thanks for ordering")

#var= IntVar()
var= StringVar()
var.set("Radio")
#var.set(1)
Label(root, text="What you want?"
      ,font="lucida 19 bold" ,justify=LEFT, padx=14).pack()
radio= Radiobutton(root, text="Dosa", padx=14, variable= var, value="Dosa").pack(anchor="w")
radio= Radiobutton(root, text="Chicken", padx=14, variable= var, value="Chicken").pack(anchor="w")
radio= Radiobutton(root, text="Burger", padx=14, variable= var, value="Burger").pack(anchor="w")

Button(text="Order Now", command=order).pack()
root.mainloop()