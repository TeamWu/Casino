from tkinter import *


class Application(Frame):
  #counter = 0
  #array = [[0 for x in range(18)] for x in range(18)]
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.createLabels()
    #self.Enter_Bet()
    #self.createWidgets()
    #self.Loop()
    
  def Enter_Bet(self):
    root2 = tk()
    Number_Bet = StringVar()
    Money_Owned.set("2500")#Change to the amount of money needed
    
    #self.master.destroy()
    #quit()
  def quite(self):
      print("Worked")
  def turn_red(self):
    if self.cell["fg"] == "green":
      
      self.cell["fg"] = "red"
    else: 
      self.cell["fg"] = "green"
      #create a new button    
      self.cell2 = Button(self)
      self.cell2["text"] = self.counter
      self.cell2["fg"] = "black"
        
      #this isn't working for some reason
      if (self.counter > 5):
          self.cell2.pack({"fill": "none"})
      else:
          self.cell2["command"] = self.turn_red
          self.cell2.pack({"fill": "x"})
      self.counter = self.counter + 1

        
  def createLabels(self):#this creates the grid of labels
        #self.QUIT = Button(self)
        #self.QUIT["text"] = "QUIT"
        #self.QUIT["fg"]   = "red"
        #self.QUIT["command"] =  self.quit

        #self.QUIT.pack({"side": "left"})

        #self.hi_there = Button(self)
        #self.hi_there["text"] = "Hello",
        #self.hi_there["command"] = self.say_hi

        #self.hi_there.pack({"side": "left"})
        
        #self.cell = Button(self)
        #self.cell["text"] = "O"
        #self.cell["fg"] = "green"
        #self.cell["command"] = self.turn_red

        #self.cell.pack({"side": "left"})

        #array = [[0 for x in range(18)] for x in range(18)]
        #for r in range(17):
        #    for c in range(17):
        #        array[r][c] = 'O'
        self.cell = Label(self, text = "Dealer:").grid(row=0,column=3)
    #Dealers Hand
        self.cell = Label(self, text = "Picture1 = ?").grid(row=1,column=1)
        self.cell = Label(self, text = "Picture2 = ?").grid(row=1,column=2)
        self.cell = Label(self, text = "Picture3 = ?").grid(row=1,column=3)
        self.cell = Label(self, text = "Total = ?").grid(row=1,column=5)
    #Players Hand
        self.cell = Label(self, text = "Player 1:(Change with actual name)").grid(row=2,column=3)
        self.cell = Label(self, text = "Picture1 = ?").grid(row=3,column=1)
        self.cell = Label(self, text = "Picture2 = ?").grid(row=3,column=2)
        self.cell = Label(self, text = "Picture3 = ?").grid(row=3,column=3)
        self.cell = Label(self, text = "Total = ?").grid(row=3,column=5)
    #If Player splits
        self.cell = Label(self, text = "Player 1 SPLIT:(Change with actual name)").grid(row=4,column=3)
        self.cell = Label(self, text = "Picture1 = ?").grid(row=5,column=1)
        self.cell = Label(self, text = "Picture2 = ?").grid(row=5,column=2)
        self.cell = Label(self, text = "Picture3 = ?").grid(row=5,column=3)
        self.cell = Label(self, text = "Total = ?").grid(row=5,column=5)
    #Options:
        #Dot selects
        #Dot select labels
        Selection = StringVar()
        Hit = Radiobutton(self, text='Hit', variable=Selection, value='Hit').grid(row=6,column=1)
        Stand = Radiobutton(self, text='Stand', variable=Selection, value='Stand').grid(row=6,column=3)
        Split = Radiobutton(self, text='Split', variable=Selection, value='Split').grid(row=6,column=5)
        
        self.cell = Button(self, text = "Enter", command =self.quite()).grid(row=8,column=3)
        self.cell = Label(self, text = "Amount won").grid(row=8,column=4)
        self.cell = Label(self, text = "$Variable Money").grid(row=8,column=5)
        
        
        
        
        """
        marker = 'X'
        for r in range(17):
            for c in range(17):
                if(r == 0):
                  #side numbered row
                  self.cell = Label(self, text=c,borderwidth=2 ).grid(row=r,column=c)
                elif(c == 0):
                  #top numbered row
                  self.cell = Label(self, text=r,borderwidth=2 ).grid(row=r,column=c)
                else:
                  self.cell = Label(self, text = marker,borderwidth=2 ).grid(row=r,column=c)
                  if (marker == 'X'):
                    marker = ' '
                  else:
                    marker = 'X'
	
     #def createWidgets(self):
       #this creates the rest of the board
                  
        self.cell = Label(self, text = "Enter the Coordinates you want to place a cell", borderwidth=1 ).grid(row=19,column=19)
        #create entry box X
        myvar = StringVar()
        self.cell = Label(self, text = "X = ",  borderwidth=1 ).grid(row=20,column=18)
        self.e1 = Entry(self, textvariable=myvar).grid(row = 20,column = 19)
        myvar.set("1")
        s = myvar.get()
        i = int(s)
        #myvar = int(myvar)
        
            #text_entry = Entry(root, textvariable=myvar)
            #text_entry.pack()
        #create entry box Y
        myvar2 = StringVar()
        self.cell = Label(self, text = "Y = ", borderwidth=1 ).grid(row=21,column=18)
        self.e2 = Entry(self, textvariable=myvar2).grid(row = 21,column = 19)
        myvar2.set("1")
        t = myvar2.get()
        j = int(t)
        #Create button
        
        #self.cell = Button(self, text="Spawn Cell", command = self.say_hi()).grid(row = 22,column = 19)#SetCell(self.e1,self.e2)).grid(row = 22,column = 19)
        self.create = Button(self)
        self.create["text"] = "Spawn Cell",
        #self.create["command"] = self.SetCell(i, j)
        self.create.grid(row = 22,column = 19)
        
        
        #self.cell["text"] = 'Spawn Cell'
        #self.cell["command"] = self.say_hi

        #Quit Button
        #self.cell = Button(self, text = "QUIT",fg = "red").grid(row = 23,column = 19)
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit_pressed
        self.QUIT.grid(row = 23,column = 19)
        
        
    """
  #def say_hi(self):
        #print("hi there, everyone!")

  #def SetCell(self,x,y): #doesn't work for some reason

        #print(x)
        #print(y)
        #self.say_hi()
    #def end(self):

    #def Loop(self):
	#for r in range(17):
          #  for c in range(17):
           #    array[r][c] 
		
    
    

root = Tk()
app = Application(root)
#root.mainloop()
