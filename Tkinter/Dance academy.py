# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:38:34 2020

@author: Lakshya Mathur
"""

from tkinter import *
root = Tk()
root.title("Dance Academy")
def getuserpass():
    with open("Data.txt" , "r+") as Data:
        Data.write(f"Username is {userval.get()} and password is {passval.get()}")
        print (Data.readline())
root.geometry("700x110")
root.maxsize(700 , 110)
root.minsize(700 , 110)
DA = Label(root , text = "Welcome to Dance Academy" , font = "comicsansms 20 bold")
DA.grid(column = 3)
user = Label(root , text = "Username")
user.grid(row = 1)
passwd =  Label(root , text = "Password")
passwd.grid(row = 2)
userval = StringVar()
passval = StringVar()
userentry = Entry(root , text = userval)
passentry =  Entry(root , text = passval)
userentry.grid(row = 1 , column = 1)
passentry.grid(row = 2 , column = 1)
Sub = Button(root , text = "Submit" , command = getuserpass)
Sub.grid(row = 3)
root.mainloop()