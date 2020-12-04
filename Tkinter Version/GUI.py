# import the modules || Source: https://www.geeksforgeeks.org/color-game-python/
import tkinter



class GUI:

    def set_up(self):
        # create a GUI window 
        self.root = tkinter.Tk() 
  
        # set the title 
        self.root.title("Black Jack Game") 
  
        # set the size 
        self.root.geometry("500x500") 
  
        # add instructions label 
        instructions1 = tkinter.Label(self.root, text = "=====================================================================================================", 
                                      font = ('Helvetica', 12)) 
        instructions1.pack()  

        instructions2 = tkinter.Label(self.root, text = "1) Blackjacks primary goal is to beat the dealers hand while keeping your hand under a total value of 21", 
                                      font = ('Helvetica', 12)) 
        instructions2.pack()  

        instructions3 = tkinter.Label(self.root, text = "2) Choosing hit will have you draw another card and add it to your total hands value", 
                                      font = ('Helvetica', 12)) 
        instructions3.pack()

        instructions4 = tkinter.Label(self.root, text = "3) Choosing stand will lock your hand in and compare it to the dealers", 
                                      font = ('Helvetica', 12)) 
        instructions4.pack()

        instructions5 = tkinter.Label(self.root, text = "=====================================================================================================", 
                                      font = ('Helvetica', 12)) 
        instructions5.pack()

        question = tkinter.Label(self.root, text = "Do you want to play a round (y/n)?")

        question.pack()
        entry = tkinter.Entry(self.root)
        entry.bind("<Return>")
        
        entry.pack()
        gui = GUI()

        self.state = entry.get()
        self.state = gui.user_input(self.state)
        # start the GUI

        self.root.mainloop() 

        if self.state == True or False:
            return self.state
        else:
            self.root.mainloop()

    def user_input(self, state):
        if state in "Yy":
            return True
        elif state in "Nn":
            return False
