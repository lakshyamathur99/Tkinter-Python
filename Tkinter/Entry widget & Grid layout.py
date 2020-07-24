from tkinter import *

def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passwordvalue.get()}")
root = Tk()
root.geometry("655x333")

user= Label(root, text="Username")
password= Label(root, text="Password")

#grid function
user.grid()
password.grid(row=1)

#entry widget
#Variable classes in tkinter
#BooleanVar, DoubleVar, StringVar IntVar

uservalue= StringVar()
passwordvalue = StringVar()

userentry = Entry(root, textvariable= uservalue)
passwordentry = Entry(root, textvariable= passwordvalue)

userentry.grid(row=0, column=1)
passwordentry.grid(row=1, column=1)

Button(text="Submit", command= getvals).grid()



root.mainloop()
