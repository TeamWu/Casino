import time
from tkinter import *
import random
"""
    1-36 = 1-36
    37 = 0
    38 = 00
    39 = 1-18
    40 = 1-12
    41 = even
    42 = red
    43 = black
    44 = 12-24
    45 = odd
    46 = 19-36
    47 = 24-36
    48 = First column
    49 = Second column
    50 = Third column
    
"""
Money_Owned = 2500
Bet = 0
root = Tk()
def Buttons(x):
    print(x)
    if x == 12:
        print("Fail")
def Input_Bet(PayOut, Number, Number_Bet):
    global Bet
    global Money_Owned
    s = Number_Bet.get()
    #Number_Bet = int(Number_Bet)
    Bet = s
    #print(Bet)
    Roulette_Number = random.randrange(1,39)
    #Result = Tk()
    if (Roulette_Number == 37):
        Str = "It landed on zero"
    elif (Roulette_Number == 38):
        Str = "It landed on double zero"
    else:
        Str = "It landed on " + str(Roulette_Number)
    
    ResultInfo = "You won $"
    if (Number == Roulette_Number):#actual number
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 39) and (Roulette_Number <= 18):#1-18
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 40) and (Roulette_Number <= 12):#1-12
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 41) and ((Roulette_Number%2) == 0) and (Roulette_Number != 37) and (Roulette_Number !=38):#even
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 42) and ((Roulette_Number%2) == 1) and (Roulette_Number != 37) and (Roulette_Number !=38):#Red/odd
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 43) and ((Roulette_Number%2) == 0)and (Roulette_Number != 37) and (Roulette_Number !=38):#Black/even
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 44) and (Roulette_Number >= 12) and (Roulette_Number <= 24):#12-24
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 45) and ((Roulette_Number%2) == 1) and (Roulette_Number != 37) and (Roulette_Number !=38):#odd
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 46) and (Roulette_Number >= 19) and (Roulette_Number <= 36):#19-36
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 47) and (Roulette_Number >= 24) and (Roulette_Number <= 36):#24-36
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 48) and ((Roulette_Number%3) == 1) and (Roulette_Number != 37) and (Roulette_Number !=38):#First column
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 49) and ((Roulette_Number%3) == 2) and (Roulette_Number != 37) and (Roulette_Number !=38):#Second column
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    elif(Number == 50) and ((Roulette_Number%3) == 3) and (Roulette_Number != 37) and (Roulette_Number !=38):#Third column
        ResultInfo = ResultInfo + str(int(Bet) * PayOut)
        Money_Owned = Money_Owned + (int(Bet) * PayOut)
    else: #lost
        
        Money_Owned = Money_Owned - int(Bet)
        if Money_Owned < 0:
            Bet = int(Bet) - (0 - Money_Owned)
        
            Money_Owned = 0
        #Bet = 0
        ResultInfo = "You lost $" + str(Bet)
    
    Label2 = Label(root, text = Money_Owned,width = 10).grid(row=15,column=2)
    Label3 = Label(root, text = Str,width = 20).grid(row=17,column=1)
    Label4 = Label(root, text = ResultInfo,width = 20).grid(row=18,column=1)
    #print(Bet)

def main():
    #print("Welcome to the game of Roulette!")
    global root
    Money_Won = 0
    #Bet = eval(input("Where would you like to place your bet?"))
    #Print_Results()
    #Money_Owned
    
    
    root.title("Board")
    Number_Bet = StringVar()
    Money_Owned = StringVar()
    Money_Owned.set("2500")
    x = 4
    y = 2
    i = 1
    Button_Array =[1 for _ in range(37)]
    Button_Zero = Button(root, text= '0',fg = "white",command = lambda i = i, cvs = 37: Input_Bet(35,cvs,Number_Bet), background = "green",borderwidth=2, padx= 15).grid(row=1,column=4)
    Button_Double_Zero = Button(root, text= '00',fg = "white",command = lambda i = i, cvs = 38: Input_Bet(35,cvs,Number_Bet), background = "green",borderwidth=2, padx= 10 ).grid(row=1,column=5)
    pad = 15

    while i < 37:
        if i > 9:
            pad = 10
        if ((i%2) == 1):
            Button_Array[i] = Button(root, text=i,fg = "white",command= lambda i = i, cvs=i: Input_Bet(35,cvs,Number_Bet), background = "red",borderwidth=2, padx= pad ).grid(row=y,column=x)
        else:
            Button_Array[i] = Button(root, text=i,fg = "white",command = lambda i = i,cvs=i: Input_Bet(35,cvs,Number_Bet), background= "black",borderwidth=2, padx= pad ).grid(row=y,column=x)
        i += 1
        if x == 6:
            x = 3
            y += 1
        x += 1
    Button_First_Column = Button(root, text="2 to 1",fg = "white",command = lambda i = i, cvs = 48: Input_Bet(2,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=14,column=4)
    Button_Second_Column = Button(root, text="2 to 1",fg = "white",command = lambda i = i, cvs = 49: Input_Bet(2,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=14,column=5)
    Button_Third_Column = Button(root, text="2 to 1",fg = "white",command = lambda i = i, cvs = 50: Input_Bet(2,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=14,column=6)

        
    ##Side buttons:
    Button_One_18 = Button(root, text="1 to 18",fg = "white",command = lambda i = i, cvs = 39: Input_Bet(1,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=2,column=1)
    Button_First12 = Button(root, text="First 12",fg = "white",command = lambda i = i, cvs = 40: Input_Bet(2,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=2,column=2)#,rowspan = 4)
    Button_Even = Button(root, text = "Even", fg = "white",command = lambda i = i, cvs = 41: Input_Bet(1,cvs,Number_Bet), bg = "green", borderwidth = 2).grid(row=3,column=1)
    Button_Red = Button(root, text = "Red",fg = "white",command = lambda i = i, cvs = 42: Input_Bet(1,cvs,Number_Bet), bg = "red",borderwidth =2).grid(row=6,column=1)#
    Button_Black = Button(root, text = "Black", fg = "white",command = lambda i = i, cvs = 43: Input_Bet(1,cvs,Number_Bet), bg = "Black", borderwidth = 2).grid(row=7,column=1)#
    Button_Second12 = Button(root, text="Second 12",fg = "white",command = lambda i = i, cvs = 44: Input_Bet(2,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=6,column=2)#
    Button_Odd = Button(root, text="Odd",fg = "white", background = "green",command = lambda i = i, cvs = 45: Input_Bet(1,cvs,Number_Bet),borderwidth=2).grid(row=10,column=1)#
    Button_19_36 =Button(root, text="19 to 36",fg = "white", background = "green",command = lambda i = i, cvs = 46: Input_Bet(1,cvs,Number_Bet),borderwidth=2).grid(row=11,column=1)#
    Button_Third12 = Button(root, text="Third 12",fg = "white", background = "green",command = lambda i = i, cvs = 47: Input_Bet(2,cvs,Number_Bet),borderwidth=2).grid(row=10,column=2)#
    s = Money_Owned.get()
    
    Label1 = Label(root, text = "You currently have: $").grid(row=15,column=1)
    Label2 = Label(root, text = int(s)).grid(row=15,column=2)
    Label3 = Label(root, text = "How much money would you like to bet?").grid(row=16,column=1)
    
    Spin_Box = Spinbox(root, from_=0, to=int(s),validate="all", textvariable = Number_Bet).grid(row=16,column=2)
    
    #Roulette_Number = random.randrange(1,39)
    #root2 = Tk()
    #Results_Label1 = Label(root2, text = Roulette_Number).grid(row=1,column=1)
    #Results_Label2 = Label(root2, text = "Your payout is going to be :").grid(row=2,column=1)
    #Results_Label3 = Label(root2, text = Money_Won).grid(row=3,column=1)
    #print(Roulette_Number)
    #print(Money_Owned)
    mainloop()
    
    
    


main()
