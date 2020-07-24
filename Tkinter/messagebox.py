from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("644x344")
root.title("Spyder")

def myfunc():
    print("Form up on me!!!")

def help():
    print("I will help you :)")
    tmsg.showinfo("Help", "I will help you with this GUI")
    
def rate():
    print("Rate Us")
    value = tmsg.askquestion("Experience", "Was your experience good?")
    if value == "yes":
        msg = "Great. Rate us on AppStore please."
    else:
        msg = "Tell us what went wrong? :("
    tmsg.showinfo("Experience", msg)
    
def friend():
    ans = tmsg.askretrycancel("Excuse me", "No")
    if ans:
        print("Please do retry")
    else:
        print("Thanks for the cancellation")
# Menu widget for creating a non dropdown menu
#mymenu= Menu(root)
#mymenu.add_command(label="File", command=myfunc)
#mymenu.add_command(label="Exit", command=quit)
#root.config(menu=mymenu)

mainmenu=Menu(root)
m1= Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator() 
m1.add_command(label="Save as", command=myfunc)
m1.add_command(label="Print", command=myfunc)

mainmenu.add_cascade(label="File", menu=m1)

root.config(menu=mainmenu)

m2= Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator() 
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)

mainmenu.add_cascade(label="Edit ", menu=m2)

root.config(menu=mainmenu)

m3= Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Be Friend", command=friend)
mainmenu.add_cascade(label="Help", menu=m3)

root.config(menu=mainmenu)

root.mainloop()
