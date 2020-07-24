from tkinter import *
root = Tk()

def getvals():
    print("It works")
root.geometry("644x344")

#heading
Label(root, text="Welcome to LUCKY TRAVELS", font="comicsans 13 bold", pady=15).grid(row=0, column=3)

#text for the form 
name= Label(root, text= "Name")
phone= Label(root, text= "Phone")
gender= Label(root, text= "Gender")
contact= Label(root, text= "Contact")
payment= Label(root, text= "Payment Mode")

#pack text 
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
contact.grid(row=4, column=2)
payment.grid(row=5, column=2)

#variables for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar() 
contactvalue = StringVar() 
paymentvalue = StringVar()
foodservicevalue = IntVar()

#entries for the form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
contactentry = Entry(root, textvariable=contactvalue)
paymententry = Entry(root, textvariable=paymentvalue)
 
#packing entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
contactentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)
 
#checkbox
foodservice = Checkbutton(text="Want to prebook your meals", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

#button and packing and assigning it a command
Button(text="Submit", command= getvals).grid(row=7, column=3)

root.mainloop()