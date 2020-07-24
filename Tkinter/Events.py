from tkinter import *

def larry(event):
    print(f"You clicked the button at {event.x}, {event.y}")
    
root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

widget = Button(root, text='Click here')
widget.pack()

widget.bind('<Button-1>', larry)
widget.bind('<Double-1>', quit)

root.mainloop()