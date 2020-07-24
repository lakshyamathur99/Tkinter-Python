# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:31:34 2020

@author: Lakshya Mathur
"""

from tkinter import *
window=Tk()
def rate():
    with open("1.txt", "a") as f:
        f.write(f"App got rating of {rating.get()} stars\n")
window.geometry("600x400")
Label(window, text="How was your experience?").pack()
rating=Scale(window,from_=0,to=10,orient=HORIZONTAL,tickinterval=3,width=6)
rating.pack()
Button(window,text="Submit",command=rate).pack()


window.mainloop()