from tkinter import *
root= Tk()
root.geometry("444x233")
root.title("My GUI")


#Important Label Options
#text - adds the text
#bg - background
#fg - foreground
#font - sets the font
#font=("comicsansms", 19, "bold")
#padx - x padding
#pady - y padding
#relief - border styling -SUNKEN, RAISED, GROOVE, RIDGE

label = Label(text='''In addition to his acting career, Khan is a television presenter and promotes humanitarian causes through his charity, Being Human Foundation.\n Khan's off-screen life is marred by controversy and legal troubles\n In 2015 he was convicted of culpable homicide for a negligent driving case in which he ran over five people with his car, killing one, \nbut his conviction was set aside on appeal.\n On 5 April 2018,Khan was convicted in a blackbuck poaching case and sentenced to \five years imprisonment.''',bg ="red", fg ="white", padx=44, pady=94,font=("comicsansms", 10, "bold"), borderwidth=3, relief = SUNKEN)

#IMPORTANT PACK OPTIONs
#anchor = nw
#SIDE = TOP, BOTTOM, LEFT ,RIGHT

#fill
#padx
#pady 

#label.pack(side =  BOTTOM, anchor = "sw", fill=X)
label.pack(side=LEFT, fill=Y, padx=34, pady=34)



root.mainloop()


from tkinter import *
root = Tk()
root.geometry("500x400")
root.title("My first GUI")
title_label = Label(text ="Ready!!! ",bg="red",fg="white",padx=10,pady=10,font=("ravi",19),relief=GROOVE,borderwidth=10)
title_label.pack(side=TOP,fill=X,padx=5,pady=8)

root.mainloop()