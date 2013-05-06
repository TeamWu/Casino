#Slots
#5/6/2013 @ 00:05

from tkinter import *
from random import *

class Player:
    def __init__(self):
        self.cash = 1500
        self.loss = 0
        self.win = 0
        self.lossStreak = 0
        self.bet = 1

    def getCash(self):
        return self.cash
    
    def addCash(self, money):
        self.cash += money
        return self.cash
        
    def subtractCash(self, money):
        self.cash -= money
        return self.cash
    
    def numLoss(self,losses):
        self.loss = losses + 1
        return self.loss
    
    def numWin(self, wins):
        self.win = wins + 1
        self.lossStreak = 0
        return self.win, self.lossStreak

    def numLossStreak(self, streak):
        self.lossStreak = streak + 1
        return self.lossStreak

    def getBet(self, selectBet):
        self.bet = selectBet
        return self.bet
    
class Spin:
    val = "y"
    w1 = 0
    w2 = 0
    w3 = 0
    
    #randomly gets three numbers for the three wheels of the slot machine
    def getRanNum(self):
        self.w1 = randrange(0,3)
        self.w2 = randrange(0,3)
        self.w3 = randrange(0,3)
        return self.w1,self.w2,self.w3

def slots():
    global root
    root = Tk()
    root.title("Slot Machine")
    root.geometry("450x450+500+300")
    #root.maxsize(450, 500)
    #root.minsize(200, 200)
    
    player = Player()
    spin = Spin()
    spinAgain = StringVar()
    spinAgain = "y"
    '''
    bet = 1
    win = IntVar()
    win = 0
    loss = IntVar()
    loss = 0
    lossStreak = IntVar()
    lossStreak = 0
    '''    
    value = "0"
    Selection = StringVar()
    selectBet = IntVar()
    sb = selectBet.get()
    line1Var = IntVar()
    line2Var = IntVar()
    line3Var = IntVar()

    def betAmount():
        sb = selectBet.get()

    def clickSpin1():
        clickSpin(spin, sb, spinAgain, player, line1Var, line2Var, line3Var)
    def clickSpin(spin, sb, spinAgain, player, line1Var, line2Var, line3Var):
        #print("You have spun")
        spin.getRanNum()
        wheel1 = Label(root, text = spin.w1, width = 1).grid(row=1,column=1)
        wheel2 = Label(root, text = spin.w2, width = 1).grid(row=1,column=2)
        wheel3 = Label(root, text = spin.w3, width = 1).grid(row=1,column=3)
        sb = selectBet.get()
        #print("sb = ", sb)
        userBet = player.getBet(sb)
        #print("userBet = ", userBet)
        #Wheel spun three matching numbers
        if spin.w1 == spin.w2 == spin.w3:
            print(spin.w1,spin.w2,spin.w3)
            print("YOU HAVE WON!")
            wonLabel = Label(root, text = "YOU HAVE WON!").grid(row=25,column=2)
            player.addCash(userBet)
            player.win += 1
            player.lossStreak = 0
            print()
            #print("win = ",win,"loss = ",loss,"lossStreak = ",lossStreak)
        #If on a losing streak force wheel to select three matching numbers
        elif player.lossStreak > 4:
            called = 0
            player.lossStreak = 0
            while (spin.w1 != spin.w2) or (spin.w1 != spin.w3):
                spin.getRanNum()
                called += 1
            print(spin.w1,spin.w2,spin.w3)
            print("YOU HAVE WON!")
            wonLabel = Label(root, text = "YOU HAVE WON!").grid(row=25,column=2)
            player.addCash(userBet)
            player.win += 1
            print()
            #print("win = ",win,"loss = ",loss,"lossStreak = ",lossStreak)
        #Wheel did not spin three matching numbers
        else:
            print(spin.w1,spin.w2,spin.w3)
            print("YOU LOSE")
            loseLabel = Label(root, text = "       YOU LOSE!     ").grid(row=25,column=2)
            player.subtractCash(userBet)
            player.loss += 1
            player.lossStreak += 1
            print()
        #print("win = ",player.win,"loss = ",player.loss,"lossStreak = ",player.lossStreak)
        return player.loss, player.win, player.lossStreak
    
    def chooseLine1():
        print("You have choosen line 1")
        #print("line1Var = ", line1Var)
        if line1.select() == "1":
            line1.deselect()
        else:
            line1.select()
            line1Var.get()
            #print("line1Var = ", line1Var)
    def chooseLine2():
        print("You have choosen line 2")
        line2Var.get()
        #print("line1Var = ", line2Var)
    def chooseLine3():
        print("You have choosen line 3")
        line3Var.get()
        #print("line1Var = ", line3Var)
    def allLines():
        line1.select()
        line2.select()
        line3.select()
        
    spinButton = Button(root, text= 'SPIN',fg = "white",command = clickSpin1,
                        background = "dark green",borderwidth=5, padx= 25).grid(
                            row=10,column=2)
    maxBet = Button(root, text= 'MAX BET',fg = "white", command = allLines,
                        background = "dark green",borderwidth=5, padx= 50).grid(
                            row=11,column=2)
    quitButton = Button(root, text= 'quit',fg = "white", command= root.destroy,
                        background = "dark green",borderwidth=5, padx= 15).grid(
                            row=12,column=2)
    cashLabel = Label(root, text = "Cash",width = 10).grid(row=15,column=2)
    betField = Spinbox(root, from_=0, to=player.getCash(),increment = 10,
                       validate="all",textvariable = selectBet).grid(row=16,column=2)

    line1 = Radiobutton(root, text='1', variable=Selection, command = chooseLine1, value='1')
    line1.grid(row=1,column=4)

    #line2 = Radiobutton(root, text='2', variable=Selection, command = chooseLine2, value='2')
    #line2.grid(row=5,column=4)

    #line3 = Radiobutton(root, text='3', variable=Selection, command = chooseLine3, value='3')
    #line3.grid(row=9,column=4)

    mainloop()

    print("Your total winnings are: $", player.getCash()-1500)
    print("You are walking away from the slot machine with: $",player.getCash())
    print("Game Over. Good Bye.")

'''#This is what I used for the command line game:
    def playLoop():
        #Loop to allow user to choose when to activate the slot machine
        while spinAgain != "n" and (player.getCash() != 0):
            spinAgain = input("do you want to spin? (y/n)\n")
            print()
            if spinAgain != "n":
                #print(type(bet), type(player.getCash()))
                try:
                    print("Your cash total is: ", player.getCash()) 
                    bet = eval(input("How much do you want to bet?\n"))
                    print()
                except SyntaxError:
                    print("Syntax Error; try again")
                except NameError:
                    print("Name Error; try again")    
                #if bet <= int(player.getCash()):
                    #if bet > 0:
                while bet > int(player.getCash()) or bet <= 0:
                    print("Your cash total is: ", player.getCash()) 
                    bet = eval(input("How much do you want to bet?\n"))
                    print()
                    #print("bet = ",bet, "player cash = ", player.getCash(),type(int(player.getCash())))
            if spinAgain != "n":
                spin.getRanNum()
                #Wheel spun three matching numbers
                if spin.w1 == spin.w2 == spin.w3:
                    print(spin.w1,spin.w2,spin.w3)
                    print("YOU HAVE WON!")
                    player.addCash(bet)
                    win += 1
                    lossStreak = 0
                    print()
                    #print("win = ",win,"loss = ",loss,"lossStreak = ",lossStreak)
                #If on a losing streak force wheel to select three matching numbers
                elif lossStreak > 4:
                    called = 0
                    lossStreak = 0
                    while (spin.w1 != spin.w2) or (spin.w1 != spin.w3):
                        spin.getRanNum()
                        called += 1
                    print(spin.w1,spin.w2,spin.w3)
                    #print("called = ", called)
                    #print(spin.w1,spin.w2,spin.w3)
                    #print()
                    print("YOU HAVE WON!")
                    player.addCash(bet)
                    win += 1
                    print()
                    #print("win = ",win,"loss = ",loss,"lossStreak = ",lossStreak)
                #Wheel did not spin three matching numbers
                else:
                    print(spin.w1,spin.w2,spin.w3)
                    print("YOU LOSE")
                    player.subtractCash(bet)
                    loss += 1
                    lossStreak += 1
                    print()
                    #print("win = ",win,"loss = ",loss,"lossStreak = ",lossStreak)
            else:
                print("You won ",win," times, but lost ",loss," times")
                print("Your total winnings are: $", player.getCash()-1500)
                print("You are walking away from the slot machine with: $",player.getCash())
                print("Game Over. Good Bye.")

        if player.getCash() == 0:
            print("You won ",win," times, but lost ",loss," times")
            print("You lost all your money :(")
            print("Game Over. Good Bye.")
'''

slots()
    
'''
#still to do:

#print winnings on UI
#add multiple lines
#get Radio buttons working
'''
