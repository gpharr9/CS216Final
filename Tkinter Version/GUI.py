# import the modules || Source: https://www.geeksforgeeks.org/color-game-python/
import tkinter
from tkinter import *

def set_up():
    # create a GUI window 
    root = tkinter.Tk() 
  
    # set the title 
    root.title("Black Jack Game") 
  
    # set the size 
    root.geometry("500x500") 
  
    # add instructions label 
    instructions1 = tkinter.Label(root, text = "=====================================================================================================", 
                                  font = ('Helvetica', 12)) 
    instructions1.pack()  

    instructions2 = tkinter.Label(root, text = "1) Blackjacks primary goal is to beat the dealers hand while keeping your hand under a total value of 21", 
                                  font = ('Helvetica', 12)) 
    instructions2.pack()  

    instructions3 = tkinter.Label(root, text = "2) Choosing hit will have you draw another card and add it to your total hands value", 
                                  font = ('Helvetica', 12)) 
    instructions3.pack()
    
    instructions4 = tkinter.Label(root, text = "3) Choosing stand will lock your hand in and compare it to the dealers", 
                                  font = ('Helvetica', 12)) 
    instructions4.pack()

    instructions5 = tkinter.Label(root, text = "=====================================================================================================", 
                                  font = ('Helvetica', 12)) 
    instructions5.pack()

    question = tkinter.Label(root, text = "Do you want to play a round (y/n)?")

    question.pack()
    var1 = StringVar()
    entry = tkinter.Entry(root, textvariable=var1)

    entry.pack()
    def res():
        result = var1.get()
        if result in "Yy":
            resultentry.insert(0, "True")
        elif result in "Nn":
            resultentry.insert(0, "False")
    resultbutton = Button(root, text = "Enter", command=res)
    resultbutton.pack()

    resultlabel = Label(root, text = "Test")
    resultlabel.pack()

    resultentry = Entry(root)
    resultentry.pack()
    root.mainloop()
    # start the GUI




set_up()
