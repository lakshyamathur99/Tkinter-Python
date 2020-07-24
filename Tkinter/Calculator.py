from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value=eval(screen.get())
            
        scvalue.set(value)
        screen.update()
        
    elif text == "C":
        scvalue.set("")
        screem.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        

root = Tk()
root.geometry("380x310")
root.title("Calculator")
root.wm_iconbitmap("cal.ico")
scvalue= StringVar()
scvalue.set("")
screen= Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f1 = Frame(root, bg="black")
b = Button(f1, text="9", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="8", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="7", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="6", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="black")
b = Button(f1, text="5", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="4", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="3", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="2", padx=20, pady=10, font="lucida 10 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="black")
b = Button(f1, text="1", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="0", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="+", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="-", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="black")
b = Button(f1, text="/", padx=20, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="*", padx=21, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=17, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="=", padx=21, pady=10, font="lucida 11 bold")
b.pack(side=LEFT, padx=22, pady=7)
b.bind("<Button-1>", click)

b = Button(f1, text="C", padx=20, pady=9, font="lucida 10 bold", bg="light green")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f1.pack()




root.mainloop()