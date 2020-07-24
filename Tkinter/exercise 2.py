from tkinter import*
m=Tk()
w=int(input())
h=int(input())
def setsize():
    m.geometry("{}x{}".format(w,h))
f1=Frame(bg="red", height=200, width=250)
f1.pack(anchor="w")
but=Button(f1, text="press", command=setsize)
but.pack(side=LEFT)

m.mainloop()