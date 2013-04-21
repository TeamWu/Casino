#testBlackjack.py

import random
import unittest

faces = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
         "Ten", "Jack", "Queen", "King", "Ace" )
suits = ( "Clubs", "Diamonds", "Hearts", "Spades" )
values = ( 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11 )

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

   def dispDeck( self, start, stop ):
      for i in range( start, stop ):
         print( "%s%s%s" % ( self.deck[i].face.rjust(5), " of ",
                self.deck[i].suit.ljust(8) ) )

   def shuffleDeck( self ):
      random.shuffle( self.deck )

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
         print( self.scoreList[ i ], " ", end="" )
      print( '\n' )

   def dispHand( self ):
      for i in range( 0 , len( self.hand ) ):
         print( "%s%s%s" % ( self.hand[i].face.rjust(5), " of ",
                self.hand[i].suit.ljust(8) ) )

   def dispDealerHand( self ):
      print( self.hand[0].face, " of ", self.hand[0].suit )
      print( "FACEDOWN" )

class Player:

   def __init__( self, name, stash ):
      self.playerHand = Hand( )
      self.name = name
      self.pocket = stash
      self.state = "PLAY"

   def newHand( self, newHand ):
      self.playerHand = newHand

   def placeBet( self, betAmount ):
      self.pocket -= betAmount

   def winBet( self, winAmount ):
      self.pocket += winAmount

   def dispStash( self ):
      print( "Player Amount = $", self.pocket )

class Bet:

   def __init__( self, betOdds ):
      self.amount = 0
      self.odds = betOdds
      self.payout = 0

   def setBetAmt( self, amount ):
      self.amount = amount

   def calcPayout( self ):
      self.payout = self.amount * self.odds

   def betInput( self, pocket ):
      amount = eval( input( ", place your bet -> $" ) )
      while amount > pocket:
         print( "You are trying to bet more money than you have" )
         amount = eval( input( ", place your bet -> $" ) )
      return amount

   def dispPayout( self ):
      print( "you won $", self.payout )

class Game:

   def __init__( self, playerx, playery ):
      self.player = playerx
      self.dealer = playery

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
            a = input( "Double Down? enter D or N -> " )
         if choice == "H":
            a = input( "Hit or Stand? enter H or S -> " )
         if choice == "P":
            a = input( "sPlit Hand? enter P or N -> " )
         if choice == "U":
            a = input( "sUrrender Hand? enter U or N -> " )
         a.upper()
      return a.upper()

   def playAgain( self ):
      a = "x"
      while a.upper() != "N" and a.upper() != "Y" :
         a = input( "Play another hand? enter Y or N -> " )
         a.upper()
      return a.upper()

class TestFunctions(unittest.TestCase):

   def test_Card( self ):
      self.card = Card( faces[0], suits[0], values[0] )
      self.assertEqual( self.card.face, "Two" )
      self.assertEqual( self.card.suit, "Clubs" )
      self.assertEqual( self.card.value, 2 )

   def test_deck_len( self ):
      self.deck = Deck( 1 )
      self.assertEqual( len( self.deck.deck ), 52 )

   def test_Deck( self ):
      self.deck = Deck( 1 )
      self.assertEqual( self.deck.deck[0].face, "Two" )      #first card in deck
      self.assertEqual( self.deck.deck[0].suit, "Clubs" )
      self.assertEqual( self.deck.deck[0].value, 2 )
      self.assertEqual( self.deck.deck[51].face, "Ace" )      #last card in deck
      self.assertEqual( self.deck.deck[51].suit, "Spades" )
      self.assertEqual( self.deck.deck[51].value, 11 )

   def test_shuffleDeck( self ):
      self.deck = Deck( 1 )
      print( '\n', "Should display 52 cards, in ranodmized order" )
      self.deck.shuffleDeck( )
      self.deck.dispDeck( 0, 51 )
      print( '\n', "Should display 52 cards, in ranodmized order" )
      self.deck.shuffleDeck( )
      self.deck.dispDeck( 0, 51 )

   def test_dispDeck( self ):
      print( '\n', "Should display 52 cards, without duplicates" )
      self.deck = Deck( 1 )
      self.deck.dispDeck( 0, 51 )

   def test_setTopCard( self ):
      self.deck = Deck( 1 )
      self.deck.setTopCard( 0 )
      self.assertEqual( self.deck.topCard, 0 )
      self.deck.setTopCard( 51 )
      self.assertEqual( self.deck.topCard, 51 )

   def test_getTopCard( self ):
      self.a = 0
      self.deck = Deck( 1 )
      self.deck.setTopCard( 21 )
      self.a = self.deck.getTopCard( )
      self.assertEqual( self.a, 21 )

   def test_Hand( self ):
      self.hand = Hand( )
      self.assertEqual( self.hand.score, 0 )

   def test_countAces( self ):
      self.a = 1
      self.deck = Deck( 1 )
      self.hand = Hand( )
      self.hand.hand.append( self.deck.deck[12] )   #Ace of Clubs
      self.hand.hand.append( self.deck.deck[25] )   #Ace of Diamonds
      self.hand.hand.append( self.deck.deck[31] )   #Seven of Hearts
      self.hand.hand.append( self.deck.deck[39] )   #Two of Spades
      self.a = self.hand.countAces( )
      self.assertEqual( self.a, 2 )

   def test_scoreHand( self ):
      self.deck = Deck( 1 )
      self.hand = Hand( )
      self.hand.hand.append( self.deck.deck[0] )   #Two of Clubs
      self.hand.hand.append( self.deck.deck[18] )  #Seven of Diamonds
      self.hand.hand.append( self.deck.deck[31] )  #Seven of Hearts
      self.hand.hand.append( self.deck.deck[39] )  #Two of Spades
      self.hand.scoreHand( )
      self.assertEqual( self.hand.score, 18 )

   def test_acesScoring( self ):
      self.deck = Deck( 1 )
      self.hand = Hand( )
      self.hand.hand.append( self.deck.deck[12] )   #Ace of Clubs
      self.hand.hand.append( self.deck.deck[25] )   #Ace of Diamonds
      self.hand.hand.append( self.deck.deck[31] )   #Seven of Hearts
      self.hand.hand.append( self.deck.deck[39] )   #Two of Spades
      self.hand.scoreHand( )
      self.hand.acesScoring( )
      self.assertEqual( self.hand.scoreList[0], 31 )
      self.assertEqual( self.hand.scoreList[1], 21 )
      self.assertEqual( self.hand.scoreList[2], 11 )

   def test_dispScore( self ):
      self.deck = Deck( 1 )
      self.hand = Hand( )
      self.hand.hand.append( self.deck.deck[12] )   #Ace of Clubs
      self.hand.hand.append( self.deck.deck[25] )   #Ace of Diamonds
      self.hand.hand.append( self.deck.deck[31] )   #Seven of Hearts
      self.hand.hand.append( self.deck.deck[39] )   #Two of Spades
      self.hand.scoreHand( )
      self.hand.acesScoring( )
      print('\n', "Should display \"31  21  11\" " )
      self.hand.dispScore( )
      self.assertEqual( self.hand.scoreList[0], 31 )
      self.assertEqual( self.hand.scoreList[1], 21 )
      self.assertEqual( self.hand.scoreList[2], 11 )

   def test_dispHand( self ):
      self.deck = Deck( 1 )
      self.hand = Hand( )
      self.hand.hand.append( self.deck.deck[0] )   #Two of Clubs   
      self.hand.hand.append( self.deck.deck[18] )  #Seven of Diamonds
      self.hand.hand.append( self.deck.deck[31] )  #Seven of Hearts
      self.hand.hand.append( self.deck.deck[39] )  #Two of Spades
      print('\n', "DISPLAY HAND" )
      self.hand.dispHand( )

   def test_dispDealerHand( self ):
      self.deck = Deck( 1 )
      self.hand = Hand( )
      self.hand.hand.append( self.deck.deck[12] )   #Ace of Clubs
      self.hand.hand.append( self.deck.deck[50] )   #King of Spades
      print('\n', "Should display \"Ace of Clubs\" and \"FACEDOWN\" " )
      self.hand.dispDealerHand( )

   def test_Player( self ):
      self.player = Player( "NAME", 1000 )
      self.assertEqual( self.player.name, "NAME" )
      self.assertEqual( self.player.pocket, 1000 )

   def test_placeBet( self ):
      self.player = Player( "NAME", 1000 )
      self.player.placeBet( 200 )
      self.assertEqual( self.player.pocket, 1000 - 200 )

   def test_winBet( self ):
      self.player = Player( "NAME", 1000 )
      self.player.winBet( 300 )
      self.assertEqual( self.player.pocket, 1000 + 300 )

   def test_dispStash( self ):
      self.player = Player( "NAME", 1234 )
      print('\n', "Should display \"Player Amount = $ 1234\" ")
      self.player.dispStash( )
      self.assertEqual( self.player.pocket, 1234 )

   def test_bet( self ):
      self.bet = Bet( 1.6 )
      self.assertEqual( self.bet.amount, 0 )
      self.assertEqual( self.bet.odds, 1.6 )
      self.assertEqual( self.bet.payout, 0 )

   def test_setBetAmt( self ):
      self.bet = Bet( 1.5 )
      self.bet.setBetAmt( 999 )
      self.assertEqual( self.bet.amount, 999)
      self.assertEqual( self.bet.odds, 1.5 )
      self.assertEqual( self.bet.payout, 0 )

   def test_calcPayout( self ):
      self.bet = Bet( 1.5 )
      self.bet.setBetAmt( 100 )
      self.bet.calcPayout( )
      self.assertEqual( self.bet.amount, 100)
      self.assertEqual( self.bet.odds, 1.5 )
      self.assertEqual( self.bet.payout, 150 )

   def test_betInput( self ):
      print("Try with input > 100, then with input <= 100", '\n')
      self.bet = Bet( 1.5 )
      self.a = 0
      self.a = self.bet.betInput( 100 )
      self.assertTrue( self.a <= 100)

   def test_dispPayout( self ):
      self.bet = Bet( 1.5 )
      self.bet.setBetAmt( 100 )
      self.bet.calcPayout( )
      self.assertEqual( self.bet.amount, 100)
      self.assertEqual( self.bet.odds, 1.5 )
      self.assertEqual( self.bet.payout, 150 )
      print('\n', "Should display \"you won $150.0\" ")
      self.bet.dispPayout( )

   def test_Game( self ):
      self.player1 = Player( "NAME1", 1000 )
      self.player2 = Player( "NAME2", 2000 )
      self.game = Game( self.player1, self.player2 )
      self.assertEqual( self.game.player.name, "NAME1" )
      self.assertEqual( self.game.player.pocket, 1000 )
      self.assertEqual( self.game.dealer.name, "NAME2" )
      self.assertEqual( self.game.dealer.pocket, 2000 )

   def test_initialDeal( self ):
      self.deck = Deck( 1 )
      self.playerx = Player( "P1", 1000 )
      self.playery = Player( "P2", 1000 )
      self.game = Game( self.playerx, self.playery)
      self.game.initialDeal( self.deck )
      self.assertEqual( self.playerx.playerHand.hand[0], self.deck.deck[0] )
      self.assertEqual( self.playerx.playerHand.hand[1], self.deck.deck[2] )
      self.assertEqual( self.playery.playerHand.hand[0], self.deck.deck[1] )
      self.assertEqual( self.playery.playerHand.hand[1], self.deck.deck[3] )

   def test_hit( self ):
      self.deck = Deck( 1 )
      self.playerx = Player( "P1", 1000 )
      self.playery = Player( "P2", 1000 )
      self.game = Game( self.playerx, self.playery)
      self.game.hit( self.playerx, self.deck )
      self.assertEqual( self.playerx.playerHand.hand[0], self.deck.deck[0] )
      self.game.hit( self.playery, self.deck )
      self.assertEqual( self.playery.playerHand.hand[0], self.deck.deck[1] )

   def test_playerInput( self ):
      self.a = "X"
      self.playerx = Player( "P1", 1000 )
      self.playery = Player( "P2", 1000 )
      self.game = Game( self.playerx, self.playery)
      self.a = self.game.playerInput( "D" )
      self.assertIn( self.a, ("N", "D") )
      self.a = self.game.playerInput( "H" )
      self.assertIn( self.a, ("H", "S") )
      self.a = self.game.playerInput( "P" )
      self.assertIn( self.a, ("N", "P") )
      self.a = self.game.playerInput( "U" )
      self.assertIn( self.a, ("N", "U") )

   def test_playAgain( self ):
      self.a = "X"
      self.playerx = Player( "P1", 1000 )
      self.playery = Player( "P2", 1000 )
      self.game = Game( self.playerx, self.playery)
      self.a = self.game.playAgain( )
      self.assertIn( self.a, ("N", "Y") )

      
if __name__ == '__main__':
   unittest.main()
