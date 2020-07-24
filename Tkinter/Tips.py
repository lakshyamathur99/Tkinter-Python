from tkinter import *
root = Tk()
root.geometry("645x345")
root.title("More about Tkinter")
root.wm_iconbitmap("1.ico")
root.config(background="grey")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command=root.destroy).pack()

root.mainloop()