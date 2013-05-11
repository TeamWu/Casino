from tkinter import *
import time
from random import *
from random import shuffle
#import Roulett_Iteration_1
import random
Name = "Player1"
Money_Owned = 2500
Bet = 0
root2 = Tk()
faces = ("2", "3", "4", "5", "6", "7", "8", "9",
         "10", "J", "Q", "K", "A" )
suits = ( "C", "D", "H", "S" )
values = ( 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11 )
playerActions = ( "Double Down", "Hit", "Split", "Stand", "Surrender" )
out = 10
play = ' '
dest = 0
####THE MENU####################################################
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        global out
        myvar = StringVar()
        self.cell = Label(self, text = "Enter your name:").grid(row=0,column=3)
        self.cell = Entry(self, textvariable=myvar, text = "Player1").grid(row=0,column=4)
        self.cell = Button(self, command = lambda myvar = myvar, cvs = myvar: self.createEntryBox(cvs), text = "Enter").grid(row=0,column=5)
        #self.createEntryBox()
    def BlackJack(self):
        print("Black Jack runs")
        BlackJack()
    def Roulett(self):
        print("Roulett runs")
        Roulett_Run()
        #Roulett_Start()
    def Slots(self):
        slots()
        print("Slots runs")
        
    def Dice(self):
        print("Dice runs")
        
    def createEntryBox(self, myvar):
        global Name
        #Name = myvar.get()
        Name = "Welcome " + myvar.get() + " which game would you like to play?"
        
        self.cell = Label(self, text = Name).grid(row=1,column=3)
        
        #self.cell = Label(self, text = Name).grid(row=1,column=4)
        self.cell = Button(self, text = "Black Jack",command = self.BlackJack).grid(row=2,column=3)
        self.cell = Button(self, text = "Roulett",command = self.Roulett).grid(row=3,column=3)
        self.cell = Button(self, text = "Slots",command = self.Slots).grid(row=4,column=3)
        self.cell = Button(self, text = "Dice",command = self.Dice).grid(row=5,column=3)

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
    
    Label2 = Label(root2, text = Money_Owned,width = 10).grid(row=15,column=2)
    Label3 = Label(root2, text = Str,width = 20).grid(row=17,column=1)
    Label4 = Label(root2, text = ResultInfo,width = 20).grid(row=18,column=1)
    #print(Bet)
    
###ROULETT################################################################
def Roulett_Run():
    #print("Welcome to the game of Roulette!")
    global root2
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
    Button_Zero = Button(root2, text= '0',fg = "white",command = lambda i = i, cvs = 37: Input_Bet(35,cvs,Number_Bet), background = "green",borderwidth=2, padx= 15).grid(row=1,column=4)
    Button_Double_Zero = Button(root2, text= '00',fg = "white",command = lambda i = i, cvs = 38: Input_Bet(35,cvs,Number_Bet), background = "green",borderwidth=2, padx= 10 ).grid(row=1,column=5)
    pad = 15

    while i < 37:
        if i > 9:
            pad = 10
        if ((i%2) == 1):
            Button_Array[i] = Button(root2, text=i,fg = "white",command= lambda i = i, cvs=i: Input_Bet(35,cvs,Number_Bet), background = "red",borderwidth=2, padx= pad ).grid(row=y,column=x)
        else:
            Button_Array[i] = Button(root2, text=i,fg = "white",command = lambda i = i,cvs=i: Input_Bet(35,cvs,Number_Bet), background= "black",borderwidth=2, padx= pad ).grid(row=y,column=x)
        i += 1
        if x == 6:
            x = 3
            y += 1
        x += 1
    Button_First_Column = Button(root2, text="2 to 1",fg = "white",command = lambda i = i, cvs = 48: Input_Bet(2,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=14,column=4)
    Button_Second_Column = Button(root2, text="2 to 1",fg = "white",command = lambda i = i, cvs = 49: Input_Bet(2,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=14,column=5)
    Button_Third_Column = Button(root2, text="2 to 1",fg = "white",command = lambda i = i, cvs = 50: Input_Bet(2,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=14,column=6)

        
    ##Side buttons:
    Button_One_18 = Button(root2, text="1 to 18",fg = "white",command = lambda i = i, cvs = 39: Input_Bet(1,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=2,column=1)
    Button_First12 = Button(root2, text="First 12",fg = "white",command = lambda i = i, cvs = 40: Input_Bet(2,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=2,column=2)#,rowspan = 4)
    Button_Even = Button(root2, text = "Even", fg = "white",command = lambda i = i, cvs = 41: Input_Bet(1,cvs,Number_Bet), bg = "green", borderwidth = 2).grid(row=3,column=1)
    Button_Red = Button(root2, text = "Red",fg = "white",command = lambda i = i, cvs = 42: Input_Bet(1,cvs,Number_Bet), bg = "red",borderwidth =2).grid(row=6,column=1)#
    Button_Black = Button(root2, text = "Black", fg = "white",command = lambda i = i, cvs = 43: Input_Bet(1,cvs,Number_Bet), bg = "Black", borderwidth = 2).grid(row=7,column=1)#
    Button_Second12 = Button(root2, text="Second 12",fg = "white",command = lambda i = i, cvs = 44: Input_Bet(2,cvs,Number_Bet), background = "green",borderwidth=2).grid(row=6,column=2)#
    Button_Odd = Button(root2, text="Odd",fg = "white", background = "green",command = lambda i = i, cvs = 45: Input_Bet(1,cvs,Number_Bet),borderwidth=2).grid(row=10,column=1)#
    Button_19_36 =Button(root2, text="19 to 36",fg = "white", background = "green",command = lambda i = i, cvs = 46: Input_Bet(1,cvs,Number_Bet),borderwidth=2).grid(row=11,column=1)#
    Button_Third12 = Button(root2, text="Third 12",fg = "white", background = "green",command = lambda i = i, cvs = 47: Input_Bet(2,cvs,Number_Bet),borderwidth=2).grid(row=10,column=2)#
    s = Money_Owned.get()
    
    Label1 = Label(root2, text = "You currently have: $").grid(row=15,column=1)
    Label2 = Label(root2, text = int(s)).grid(row=15,column=2)
    Label3 = Label(root2, text = "How much money would you like to bet?").grid(row=16,column=1)
    
    Spin_Box = Spinbox(root2, from_=0, to=int(s),validate="all", textvariable = Number_Bet).grid(row=16,column=2)
    
    #Roulette_Number = random.randrange(1,39)
    #root2 = Tk()
    #Results_Label1 = Label(root2, text = Roulette_Number).grid(row=1,column=1)
    #Results_Label2 = Label(root2, text = "Your payout is going to be :").grid(row=2,column=1)
    #Results_Label3 = Label(root2, text = Money_Won).grid(row=3,column=1)
    #print(Roulette_Number)
    #print(Money_Owned)
    #mainloop()


###BlackJack#####################################################

class Card:

   def __init__( self, face, suit, value ):
      self.face = face
      self.suit = suit
      self.value = value

class Deck:

   def __init__( self, numDecks ):
      self.topCard = 0
      self.deck = []
      for k in range( 0, numDecks ):
         for i in range( 0, len( suits ) ):
            for j in range( 0, len( faces ) ):
               self.deck.append( Card( faces[j], suits[i], values[j] ) )

   def shuffleDeck( self ):
      shuffle( self.deck )

   def dispDeck( self, start, stop ):
      outStr0 = self.deck[i].face + self.deck[i].suit
      for i in range( start, stop ):
#         print( "%s%s%s" % ( self.deck[i].face.rjust(5), " of ",
#                self.deck[i].suit.ljust(8) ) )
         print( self.outStr0 )

   def setTopCard( self, top ):
      self.topCard = top

   def getTopCard( self ):
      return self.topCard

class Hand:

   def __init__( self ):
      self.score = 0
      self.hand = []
      self.scoreList = []
      
   def countAces( self ):
      numAces = 0
      for i in range( 0, len( self.hand ) ):
         if self.hand[ i ].face == "Ace":
            numAces += 1
      return numAces
   
   def scoreHand( self ):
      self.score = 0
      for i in range( 0, len( self.hand ) ):
         self.score += self.hand[ i ].value

   def acesScoring( self ):
      a = self.countAces( )
      for i in range( 0, a + 1 ):
         if len( self.scoreList ) == i :
            self.scoreList.append( self.score - i * 10 )
         else:
            self.scoreList[ i ] = self.score - i * 10

      self. score = self.scoreList[ len( self.scoreList ) - 1 ]
      for i in range( len( self.scoreList ) - 1, -1, -1 ):
         if self.scoreList[ i ] <= 21:
            self. score = self.scoreList[ i ]

   def dispScore( self ):
      for i in range( 0, len( self.scoreList ) ):
         outStr1 = self.scoreList[ i ]
#         print( self.scoreList[ i ], " ", end="" )
#      print( '\n' )
         return( outStr1 )

   def dispHand( self ):
      outStr2 = ' '
      for i in range( 0 , len( self.hand ) ):
         outStr2 = outStr2 + " " + self.hand[i].face + self.hand[i].suit
         #print( "%s%s%s" % ( self.hand[i].face.rjust(5), " of ",
         #       self.hand[i].suit.ljust(8) ) )
      return( outStr2 )

   def dispDealerHand( self ):
      outStr2 = self.hand[0].face + self.hand[0].suit + " FACEDOWN"
      #outStr3 = "FACEDOWN"
#      print( self.hand[0].face, " of ", self.hand[0].suit )
#      print( "FACEDOWN" )
      return( outStr2 )
      #print( outStr3 )

class Player:

   def __init__( self, name, stash ):
      self.playerHand = Hand( )
      self.name = name
      self.pocket = stash
      self.state = "PLAY"
      self.POSITION = "None"

#   def getPlayerPocket( self ):
#      return self.pocket

   def newHand( self, newHand ):
      self.playerHand = newHand

   def placeBet( self, betAmount ):
      self.pocket -= betAmount

   def winBet( self, winAmount ):
      self.pocket += winAmount

   def dispStash( self ):
      outStr4 = "Player Amount = $" + str( self.pocket )
#      print( "Player Amount = $", self.pocket )
      return( outStr4 )

class Bet:

   def __init__( self, betOdds ):
      self.amount = 0
      self.odds = betOdds
      self.payout = 0

#   def getBetAmount( self ):
#      return self.amount

   def setBetAmt( self, amount ):
      self.amount = amount

   def calcPayout( self ):
      self.payout = self.amount * self.odds

   def betInput( self, pocket ):
      
      impStr1 = "Place your bet -> $"
      '''
      outStr5 = "You are trying to bet more money than you have"
#      amount = eval( input( ", place your bet -> $" ) )
      amount = eval( input( impStr1 ) )
      while amount > pocket:
#         print( "You are trying to bet more money than you have" )
#         amount = eval( input( ", place your bet -> $" ) )
         print( outStr5 )
         amount = eval( input( impStr1 ) )
      '''
      
      #return amount

   def dispPayout( self ):
      outStr6 = "You won $" + str (self.payout )
#      print( "you won $", self.payout )
      print( outStr6 )

class Game:

   def __init__( self, playerx, playery ):
      self.player = playerx
      self.dealer = playery
      self.impStr2 = "Double Down? enter D or N -> "
      self.impStr3 = "Hit or Stand? enter H or S -> "
      self.impStr4 = "sPlit Hand? enter P or N -> "
      self.impStr5 = "sUrrender Hand? enter U or N -> "
      self.impStr6 = "Play another hand? enter Y or N -> "
      self.outStr20 = "You don't have enough money to double down"

   def initialDeal( self, deckx ):
      for i in range( deckx.topCard, deckx.topCard + 4, 2 ):
         self.player.playerHand.hand.append( deckx.deck[ i ] )
         self.dealer.playerHand.hand.append( deckx.deck[ i + 1 ] )
      deckx.setTopCard( i + 2 )

   def hit( self, playerx, deckx ):
      playerx.playerHand.hand.append( deckx.deck[ deckx.topCard ] )
      deckx.setTopCard( deckx.topCard + 1 )

   def playerInput( self, choice ):
      a = "x"
      while a.upper() != "D" and a.upper() != "H" and a.upper() != "N" \
                      and a.upper() != "P" and a.upper() != "S" \
                      and a.upper() != "U":
         if choice == "D":
#            a = input( "Double Down? enter D or N -> " )
            a = input( self.impStr2 )
#            if a.upper() == "D" and Player.getPlayerPocket() < 2 * Bet.getBetAmount():
#               print( outStr20 )
#               a = "N"            
         if choice == "H":
#            a = input( "Hit or Stand? enter H or S -> " )
            a = input( self.impStr3 )
         if choice == "P":
#            a = input( "sPlit Hand? enter P or N -> " )
            a = input( self.impStr4 )
         if choice == "U":
#            a = input( "sUrrender Hand? enter U or N -> " )
            a = input( self.impStr5 )
         a.upper()
      return a.upper()

   def playAgain( self ):
      a = "x"
      while a.upper() != "N" and a.upper() != "Y" :
#         a = input( "Play another hand? enter Y or N -> " )
         a = input( self.impStr6 )
         a.upper()
      return a.upper()        
def close_window(root2):
   global dest
   root2.destroy()
   dest = 1
def Destroy_Window(root, test):
   global play
   if test == 0:
      play = "Y"
   elif test == 1:
      play = "N"
   root.destroy()
   
def UserPicked(Choice):
   print(Choice.get())
   global out
   global play
   global dest
   '''
   if (Selection.get() == 1):
      Hit()
   else if(Selection.get() == 2):
      Surrender()
   else if (Selection.get() == 3):
      Stand()
   '''
   #print("PASS")
   if(Choice.get() == 1):
      out = "Hit"
      dest = 1

   elif(Choice.get() == 2):
      out = "Surrender"
      dest = 2

   elif(Choice.get() == 3):
      out = "Stand"
      dest = 3
   print(dest)      
   #else if (Selection.get() == 4


def BlackJack():###BlackJack = main
   global out
   global dest
   global play
   #global root
   #app = Application(root)
   #11111111111
   #impStr7 = "Enter number of decks to play with -> "
#   numDecks = eval( input( "Enter number of decks to play with -> " ) )
   #numDecks = eval( input( impStr7 ) )
   #11111111111
   numDecks = 2
   newDeck = Deck( numDecks )                            #Create deck(s) object
   newDeck.shuffleDeck( )                                      #Shuffle deck(s)
#   newDeck.dispDeck( 0, 16 )
   player = Player( "Adam", 1000 )                       #Create player objects
   dealer = Player( "Dealer", 1 )
   name = "Adam"
   
   #app.PlayerName("Adam")
   newGame = Game( player, dealer)                          #Create game object
   #---------------------------------------      
   #root.mainloop()
   outStr7 = newGame.player.name + " Blackjack!"
   outStr8 = newGame.dealer.name + " Blackjack!"
   outStr9 = newGame.player.name + " Wins!"
   outStr10 = newGame.dealer.name + " Wins!"
   outStr19 = newGame.player.name + " loses!" 
   outStr11 = newGame.player.name + "Busted!"
   outStr12 = newGame.dealer.name + "Busted!"
   outStr16 = newGame.player.name + " is surrendering this hand"
   outStr17 = "Push - " + newGame.player.name + "'s bet returned"
   outStr18 = "Not enough cards are left in the deck to play another hand"
   
   play = "Y"
   
   while play == "Y" and newDeck.topCard < ( numDecks * ( 52 - 20 ) ):
      
      action = " "
      EnterBet = Tk() ### root2 = EnterBet
      dest = 0
      ########Change betInput
      Number_Bet = IntVar()
      amt = IntVar()
      Spin_Box = Spinbox(EnterBet, from_=0, to=player.pocket,validate="all", textvariable = Number_Bet).grid(row=1,column=2)
      Label3 = Label(EnterBet, text = "How much money would you like to bet?").grid(row=1,column=1)
      
      UsersPick = Button(EnterBet, text = "Enter",command = lambda amt = amt, cvs = amt: close_window(EnterBet)).grid(row=2,column=2)
      #amount = playerBet.betInput( player.pocket )#BRADY:change this to read the text field of the bet
      playerBet = Bet( 1.5 )           #get bet from player - create bet object
      while dest == 0:
         amt = int(Number_Bet.get())
         print('', end="")
         #app.PlayerMoney(player.dispStash()) #BRADY:returns amount of money they have
   #      print( newGame.player.name, end = "" )

   
         '''
         impStr1 = "Place your bet -> $"
         outStr5 = "You are trying to bet more money than you have"
   #      amount = eval( input( ", place your bet -> $" ) )
         amount = eval( input( impStr1 ) )
         amount = playerBet.betInput( player.pocket )
         while amount > pocket:
   #         print( "You are trying to bet more money than you have" )
   #         amount = eval( input( ", place your bet -> $" ) )
            print( outStr5 )
            amount = eval( input( impStr1 ) )
          #still prints to screen
         '''
         
         #playerBet.setBetAmt( amt )
      dest = 0
      print(amt)
      player.placeBet( amt )
      #_______________________________________
      BlackJackGUI = Tk()  #BlackJackGUI = root
      Choice = IntVar()
      cell = Label(BlackJackGUI, text = player.dispStash()).grid(row=8,column=5)
      cell = Label(BlackJackGUI, text = "Player 1: " + name).grid(row=2,column=3)

      Hit = Radiobutton(BlackJackGUI, text='Hit', variable=Choice, value=1).grid(row=6,column=1)
      Surrender = Radiobutton(BlackJackGUI, text='Surrender', variable=Choice, value=2).grid(row=6,column=2)
      Stand = Radiobutton(BlackJackGUI, text='Stand', variable=Choice, value=3).grid(row=6,column=3)
      DoubleDown = Radiobutton(BlackJackGUI, text='DoubleDown', variable=Choice, value=4).grid(row=6,column=4)
      Split = Radiobutton(BlackJackGUI, text='Split', variable=Choice, value=5).grid(row=6,column=5) 
      BuyInsurance = Radiobutton(BlackJackGUI, text='BuyInsurance', variable=Choice, value=6).grid(row=6,column=6)
      UsersPick = Button(BlackJackGUI, text = "Enter",command = lambda Choice = Choice, cvs = Choice: UserPicked(cvs)).grid(row=8,column=3)
      cell = Label(BlackJackGUI, text = "Amount won:").grid(row=8,column=4)
      newGame.initialDeal( newDeck )
#      print( '\n', newGame.player.name )            #Display 2 card player hand
      cell = Label(BlackJackGUI,width = 30, text = "Players Hand: " + player.playerHand.dispHand( )).grid(row=3,column=2)
      #app.PlayersHand(player.playerHand.dispHand( )) #BRADY:returns the hand the user has
      player.playerHand.scoreHand( )
      player.playerHand.acesScoring( )
      
      cell = Label(BlackJackGUI,width = 20, text = "Total = " + str(player.playerHand.dispScore( ))).grid(row=3,column=5)
      #app.PlayerTotal(player.playerHand.dispScore( )) #BRADY:returns the score of the player



#      print( '\n', newGame.dealer.name )#Disp 1 card up, 1 card down dealer hand

      cell = Label(BlackJackGUI, width = 30, text = "Dealers Hand: " + dealer.playerHand.dispDealerHand( )).grid(row=1,column=2)
      #print(dealer.playerHand.dispDealerHand( )) #BRADY:returns the dealers hand
      
      
      if player.playerHand.score == 21:                  #Player has a Blackjack
#         print( '\n', newGame.player.name, " Blackjack!", '\n' )
         print( outStr7 )

      dealer.playerHand.scoreHand( )
      if player.playerHand.score == 21 and dealer.playerHand.score == 21:
                                             #Dealer also has a Blackjack - push
         
         cell = Label(BlackJackGUI,width = 20, text = "Dealers Hand: " + dealer.playerHand.dispHand( )).grid(row=1,column=2)
         #print(dealer.playerHand.dispHand( )) #BRADY:returns the dealers hand
#         print( '\n', newGame.dealer.name, " Blackjack!", '\n' )
         print( outStr8 ) #BlackJack
         player.state = "PUSH"

      if player.playerHand.score == 21 and dealer.playerHand.score <= 21:
         dealer.playerHand.dispHand( )
#         print( newGame.player.name, " Wins!" )
         print( outStr9 ) #BRADY:BlackJack
         player.state = "WIN"
         #out = ' '
########## SPLIT ############################################################## not going to worry about this part
      while(player.state != "WIN" and player.state != "LOSE" and player.state != "SURRENDER" and out != 3):
         print('', end="")
         if (Selection.get() != 0):
             #out = Selection.get()
             print(int(Selection.get()))
             print(out)
         #if player.state == "PLAY":                                #not a blackjack
         #   if player.playerHand.hand[0].face == player.playerHand.hand[1].face:
               #action = newGame.playerInput( "P" )#BRADY:comment out
         #      if UsersPick == 5:#BRADY:if certian radiobox
                  
         #         outStr15 = newGame.player.name + " is splitting his " + player.playerHand.hand[0].face + "'s"
         #         player.state = "SPLIT"
   #               print( newGame.player.name, " is splitting his ",
   #               player.playerHand.hand[0].face, "'s", '\n' )
         #         print( outStr15 )#BRADY:comment out
               
   ########## SURRENDER ##########################################################            
         if player.state == "PLAY" and (dest == 2):                                #not a blackjack
            #action = newGame.playerInput( "U" )#BRADY:comment out
            
            #player.Reset()
            #if UsersPick == 2:#BRADY:if certian radiobox
            player.state = "SURRENDER"
            out = 0;
   #            print( newGame.player.name, " is surrendering this hand" )
            print( outStr16 )#BRADY:comment out
             
   ########## DOUBLE DOWN ######################################################## not going to worry about this part
         if player.state == "PLAY" and out == "Double Down":                         #Player not a blackjack
            #action = newGame.playerInput( "D" )#BRADY:comment out
            if UsersPick == 4:#BRADY:if certian radiobox
               player.state = "DOUBLEDOWN"
               playerBet.setBetAmt( 2 * amt )                    #Double bet amount
               player.placeBet( amt )  #take from player's stash another bet amount
   #            print( '\n', newGame.player.name )
               newGame.hit( player, newDeck )
               #print(player.playerHand.dispHand( ))#BRADY:returns the hand the user has
               cell = Label(BlackJackGUI,width = 30, text = "Players Hand: " + player.playerHand.dispHand( )).grid(row=3,column=2)
               player.playerHand.scoreHand( )
               player.playerHand.acesScoring( )
               #print(player.playerHand.dispScore( ))
               cell = Label(root,width = 20, text = "Total = " + str(player.playerHand.dispScore( ))).grid(row=3,column=5)
               if player.playerHand.score > 21:                      #Player busted
   #               print( '\n', newGame.player.name, "Busted!" )
   #               print( newGame.dealer.name, " Wins!", '\n' )
                  print( outStr11 + outStr10 )
                  #print( outStr10 )
                  player.state = "LOSE"
               
   ########## PLAYER GAME PLAY ###################################################
         if player.state == "PLAY" and (dest == 1):                      #no change from above code
              ###function hit button call
            #print("HHHHIIIIITTTT")
            #action = newGame.playerInput( "H" )#BRADY:comment out                 #play player's hand
            out = 0
            #while player.playerHand.score < 21:#BRADY:if certain radiobox
   #            print( '\n', newGame.player.name )
            newGame.hit( player, newDeck )
               #print(player.playerHand.dispHand( ))#BRADY:returns the hand the user has
            cell = Label(BlackJackGUI, width = 30, text = "Players Hand: " + player.playerHand.dispHand( )).grid(row=3,column=2)
               
            player.playerHand.scoreHand( )
            player.playerHand.acesScoring( )
               #print(player.playerHand.dispScore( ))
            cell = Label(BlackJackGUI,width = 20, text = "Total = " + str(player.playerHand.dispScore( ))).grid(row=3,column=5)
               
               #if player.playerHand.score < 21:            #Player still not busted
                  #action = newGame.playerInput( "H" )#BRADY:comment out
            if player.playerHand.score > 21:                      #Player busted
   #               print( '\n', newGame.player.name, "Busted!" )
   #               print( newGame.dealer.name, " Wins!", '\n' )
               print( outStr11 + outStr10 )
                  #print( outStr10 )
               player.state = "LOSE"
                  
      out = ' '
      dest = 0
########## DEALER GAME PLAY ###################################################               
      if player.state == "PLAY" or player.state == "DOUBLEDOWN":
                                    #if player's not busted, show dealer's hand
         #print( '\n', newGame.dealer.name )
         
         #print(dealer.playerHand.dispHand( ))#BRADY:returns the hand the dealer has
         cell = Label(BlackJackGUI,width = 30, text = "Dealers Hand: " + dealer.playerHand.dispHand( )).grid(row=1,column=2)
         
         dealer.playerHand.scoreHand( )
         dealer.playerHand.acesScoring( )
         
         #print(dealer.playerHand.dispScore( ))
         cell = Label(BlackJackGUI,width = 20, text = "Total = " + str(dealer.playerHand.dispScore( ))).grid(row=1,column=5)
         
                                     #player's score <= 21, dealer's score < 17
         while dealer.playerHand.score < 17:
            newGame.hit( dealer, newDeck )
            
            #print(dealer.playerHand.dispHand( ))#BRADY:returns the hand the dealer has
            cell = Label(BlackJackGUI,width = 30, text = "Dealers Hand: " + dealer.playerHand.dispHand( )).grid(row=1,column=2)
            
            dealer.playerHand.scoreHand( )
            dealer.playerHand.acesScoring( )
            
            #print(dealer.playerHand.dispScore( ))
            cell = Label(BlackJackGUI,width = 20, text = "Total = " + str(dealer.playerHand.dispScore( ))).grid(row=1,column=5)
            
            if dealer.playerHand.score > 21:         #Dealer busts - player wins
#               print( '\n', newGame.dealer.name, "Busted!" )
#               print( newGame.player.name, " Wins!" )
               print( outStr12 )
               print( outStr9 )
               player.state = "WIN"
                                                 #neither player or dealer busts
         if player.playerHand.score <= 21 and dealer.playerHand.score <= 21:
            if player.playerHand.score <= dealer.playerHand.score:
                                                     #dealer wins - player loses
#               print( newGame.player.name, " Loses", '\n' )
               print( outStr19 )
               player.state = "LOSE"
            else:                                    #player wins - dealer loses
#               print( newGame.player.name, " Wins!" )
               print( outStr9 )
               player.state = "WIN"
              
########## SETTLE UP WITH PLAYER ###############################################
      if player.state == "LOSE":
#         print( newGame.player.name, " loses $", playerBet.amount )
         outStr13 = newGame.player.name + " loses $" + str( playerBet.amount )
         print( outStr13 )
         
         #print(player.dispStash( ))
         cell = Label(BlackJackGUI,width = 20, text = player.dispStash()).grid(row=8,column=5)

      if player.state == "WIN":
         playerBet.calcPayout( )
         cell = Label(BlackJackGUI, text = amt).grid(row=8,column=5)
         outStr14 = newGame.player.name + " wins $" + str( amt )
#         print( newGame.player.name, " wins $", playerBet.payout )
         print( outStr14 )                       #return winnings + original bet
         #player.winBet( int(playerBet.payout) + playerBet.amount )
         player.winBet( amt + amt)
         print(player.dispStash( ))
         cell = Label(BlackJackGUI,width = 20, text = player.dispStash()).grid(row=8,column=5)

      if player.state == "PUSH":
#         print( '\n', "Push - ", newGame.player.name, "'s bet returned" )
         print( outStr17 )
         player.winBet( playerBet.amount )            #return bet amount on push
         print(player.dispStash( ))

      if player.state == "SURRENDER":
         player.winBet( playerBet.amount / 2 )   #return 1/2 of bet on surrender
         print(player.dispStash( ))
#---------------------------------------
      play = " "
      UsersPick = Button(BlackJackGUI, text = "Play again",command = lambda Selection = Selection, cvs = Selection: Destroy_Window(BlackJackGUI,0)).grid(row=9,column=3)
      UsersPick = Button(BlackJackGUI, text = "Quit",command = lambda Selection = Selection, cvs = Selection: Destroy_Window(BlackJackGUI,1)).grid(row=10,column=3)
      #play = newGame.playAgain( )#still prints in this
      while(play != "Y" and play != "N"):
         print('',end = '')
      if play == "Y": #change this so the user will be able to play again and place a new bet
         hand1 = Hand( )
         hand2 = Hand( )
         newGame.player.playerHand = hand1
         newGame.dealer.playerHand = hand2
         player.state = "PLAY"
      
   if play == "Y":###delete everything after this
#      print( "Not enough cards are left in the deck to play another hand" )
      print( outStr18 )
######slots


class Player:
    def __init__(self):
        self.cash = 1500
        self.loss = 0
        self.win = 0
        self.lossStreak = 0
        self.bet = 1
        self.totalWinnings = 0

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

    def getWinnings(self):
        self.totalWinnings = self.cash - 1500
        return self.totalWinnings
    
class Spin:
    val = "y"
    w1=[0,0,0] 
    w2=[0,0,0]
    w3=[0,0,0]
    
    #randomly gets three numbers for the three wheels of the slot machine
    def getRanNum(self):
        for num in range(len(self.w1)):
            self.w1[num] = randrange(0,3)
            self.w2[num] = randrange(0,3)
            self.w3[num] = randrange(0,3)
        return self.w1,self.w2,self.w3

def slots():
    global root
    root3 = Tk()
    root3.title("Slot Machine")
    root3.geometry("450x450+500+300")
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
        
    def updateWinnings():
        #winnings = player.getWinnings()
        #winnings = Label(root, text = "Your total winnings are: ",width = 20)#, padx=15, pady=10)
        #winnings.grid(row=29,column=1)
    
        #print("totalWinnings = ", winnings)
        #winningsAmount = Label(root, text = winnings,width = 20).grid(row=29,column=2)

        totalStash = Label(root3, text = "Cash =", width = 5, padx=5)
        totalStash.grid(row=30,column=1)
        
        stashAmount = Label(root, text = player.getCash(), width = 20)
        stashAmount.grid(row=30,column=2)

    def clickSpin1():
        sb = selectBet.get()
        clickSpin(spin, sb, spinAgain, player, line1Var, line2Var, line3Var)
        updateWinnings()
        
    def clickSpin(spin, sb, spinAgain, player, line1Var, line2Var, line3Var):
        #print("You have spun")
        spin.getRanNum()
        wheel1 = Label(root3, text = spin.w1, width = 20).grid(row=1,column=2)
        wheel2 = Label(root3, text = spin.w2, width = 20).grid(row=2,column=2)
        wheel3 = Label(root3, text = spin.w3, width = 20).grid(row=3,column=2)
        #print("sb = ", sb)
        userBet = player.getBet(sb)
        #print("userBet = ", userBet)
        #Wheel spun three matching numbers
        if spin.w1[0]==spin.w1[1]==spin.w1[2] or spin.w2[0]==spin.w2[1]==spin.w2[2] or spin.w3[0]==spin.w3[1]==spin.w3[2]:
            print(spin.w1,spin.w2,spin.w3)
            print("YOU HAVE WON!")
            wonLabel = Label(root3, text = "YOU HAVE WON!").grid(row=25,column=2)
            player.addCash(userBet)
            player.win += 1
            player.lossStreak = 0
            print()
            #print("win = ",win,"loss = ",loss,"lossStreak = ",lossStreak)
        #If on a losing streak force wheel to select three matching numbers
            '''
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
            '''
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
        '''
        #print("line1Var = ", line1Var)
        if line1.select() == "1":
            line1.deselect()
        else:
            line1.select()
            line1Var.get()
            #print("line1Var = ", line1Var)
            '''
        l1 = line1Var.get()
        print("l1= ", l1)
    def chooseLine2():
        print("You have choosen line 2")
        l2 = line2Var.get()
        #print("line1Var = ", line2Var)
        print("l2= ", l2)
    def chooseLine3():
        print("You have choosen line 3")
        l3 = line3Var.get()
        #print("line1Var = ", line3Var)
        print("l3= ", l3)
    def allLines():
        line1.select()
        line2.select()
        line3.select()
        
    def betMax():
        maxBet = player.getCash()
        sb = maxBet
        #print("maxBet = ", maxBet)
        clickSpin(spin, sb, spinAgain, player, line1Var, line2Var, line3Var)
        updateWinnings()


    wheel1 = Label(root3, text = spin.w1, width = 20).grid(row=1,column=2)
    wheel2 = Label(root3, text = spin.w2, width = 20).grid(row=2,column=2)
    wheel3 = Label(root3, text = spin.w3, width = 20).grid(row=3,column=2)
        
    spinButton = Button(root3, text= 'SPIN',fg = "white",command = clickSpin1,
                        background = "dark green",borderwidth=5, padx= 25).grid(
                            row=10,column=2)
    maxBet = Button(root3, text= 'MAX BET',fg = "white", command = betMax,#allLines,
                        background = "dark green",borderwidth=5, padx= 50).grid(
                            row=11,column=2)
    quitButton = Button(root3, text= 'quit',fg = "white", command= root.destroy,
                        background = "dark green",borderwidth=5, padx= 15).grid(
                            row=12,column=2)
    betLabel = Label(root3, text = "BET:",width = 10).grid(row=15,column=2)
    
    betField = Spinbox(root3, from_=1, to=player.getCash(),increment = 10,
                       validate="all",textvariable = selectBet).grid(row=16,column=2)

    line1 = Radiobutton(root3, text='1', variable=line1Var, command = chooseLine1, value='1')
    line1.grid(row=1,column=4)

    line2 = Radiobutton(root3, text='2', variable=line2Var, command = chooseLine2, value='2')
    line2.grid(row=2,column=4)

    line3 = Radiobutton(root3, text='3', variable=line3Var, command = chooseLine3, value='3')
    line3.grid(row=3,column=4)

    #mainloop()

    print("Your total winnings are: $", player.getCash()-1500)
    print("You are walking away from the slot machine with: $",player.getCash())
    print("Game Over. Good Bye.")

def main():
    global out      
    root = Tk()
    app = Application(root)
main()

        


