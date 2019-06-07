import random

class Card:
    def __init__(self):
        self.CardName = ""
        self.CardStrength = 0

    def CardDetails(self,name,strength):
        self.CardName = name
        self.CardStrength = strength

class Deck:
    def __init__(self):
        self.DeckName = ""
        self.CardInDeck = []
        self.CountOfCardsInDeck = 0
        self.IndexOfList = 0
        self.AddCardInOutdatedDeck = []

    def initialisation(self,name,MyList):
        self.DeckName = name
        self.CardInDeck = MyList
        self.CountOfCardsInDeck = len(self.CardInDeck)
    
    def AddCardIntoDeck(self,CardToBeInserted):
        self.CardInDeck.insert(0,CardToBeInserted)
    
    def OutDatedListFormation(self,insert):

            if self.IndexOfList == 0:
                self.AddCardInOutdatedDeck.insert(0,insert)
                self.IndexOfList += 1
            else:
                self.AddCardInOutdatedDeck.insert(self.IndexOfList, insert) 
                self.IndexOfList += 1
                random.shuffle(self.AddCardInOutdatedDeck)
            self.CountOfCardsInDeck = self.IndexOfList

    def show(self):
        for value in self.CardInDeck:
            print(value.CardName,value.CardStrength)
    
    def ShowOutDatedDeck(self):
        for value in self.AddCardInOutdatedDeck:
            print(value.CardName,value.CardStrength)

class Player: 

    def __init__(self,name,deck):
        self.GodSpell = 1
        self.ResurrectSpell = 1
        self.PlayerDeck = deck
        self.PlayerName = name
        self.FirstPlayerScore = 0
        self.SecondPlayerScore = 0
        self.PlayerOneFlag = "False"
        self.PlayerTwoFlag = "False"
    
    def RollingDice(self):
        min = 1
        max = 6
        PlayerOneChoice = random.randint(min,max)
        PlayerTwoChoice = random.randint(min,max)

        while PlayerOneChoice == PlayerTwoChoice:
            if PlayerOneChoice == PlayerTwoChoice:
                PlayerOneChoice = random.randint(min,max)
                PlayerTwoChoice = random.randint(min,max)

        print("Player One Choice", PlayerOneChoice)
        print("Player Two Choice", PlayerTwoChoice)
        if PlayerOneChoice > PlayerTwoChoice:
            return 1
        else:
            return 0

    def showDetails(self):
        print("Player Name",self.PlayerName)
        print("Spells", self.GodSpell,self.ResurrectSpell)
        for index in range(0,len(self.PlayerDeck.CardInDeck)):
            print(self.PlayerDeck.CardInDeck[index].CardName)

A = Card()
A.CardDetails("A",1)
B = Card()
B.CardDetails("B",2)
C = Card()
C.CardDetails("C",3)
D = Card()
D.CardDetails("D",4)
E = Card()
E.CardDetails("E",5)
F = Card()
F.CardDetails("F",6)
G = Card()
G.CardDetails("G",7)
H = Card()
H.CardDetails("H",8)
I = Card()
I.CardDetails("I",9)
J = Card()
J.CardDetails("J",10)
K = Card()
K.CardDetails("K",11)
L = Card()
L.CardDetails("L",12)
M = Card()
M.CardDetails("M",13)
N = Card()
N.CardDetails("N",14)
O = Card()
O.CardDetails("O",15)
P = Card()
P.CardDetails("P",16)

MyDeck = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]

random.shuffle(MyDeck)
CompleteDeck = Deck()
OutDatedDeck = Deck()
CompleteDeck = CompleteDeck.initialisation("Complete Deck",MyDeck)
#CompleteDeck.show(CompleteDeck)
PlayerOneCardsList = []
PlayerTwoCardsList = []

RoundStartingPlayer = Player("",[])
RoundSecondPlayer = Player("",[])

for i in range(len(MyDeck)):
    if(i < len(MyDeck)/2):
        PlayerOneCardsList.append(MyDeck[i])
    else:
        PlayerTwoCardsList.append(MyDeck[i])
    
PlayerOneCards = Deck()
PlayerTwoCards = Deck()
PlayerOneCards.initialisation("Player One Cards",PlayerOneCardsList)
PlayerTwoCards.initialisation("Player One Cards",PlayerTwoCardsList)

FirstPlayer = Player("Rishabh",PlayerOneCards)
SecondPlayer = Player("Rohit",PlayerTwoCards)



ResultOfRollingDice = FirstPlayer.RollingDice()

if ResultOfRollingDice == 1:

    RoundStartingPlayer = FirstPlayer
    RoundSecondPlayer = SecondPlayer
    RoundStartingPlayer.PlayerOneFlag = "True"
    RoundSecondPlayer.PlayerTwoFlag = "False"

else:

    RoundStartingPlayer = SecondPlayer
    RoundSecondPlayer = FirstPlayer 
    RoundStartingPlayer.PlayerOneFlag = "False"
    RoundSecondPlayer.PlayerTwoFlag = "True"

def GodSpellMode():

    RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck
    print("Total Number Of Cards = ", RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck)
    FirstPlayerChoiceToBePlayed = input("\nEnter The Choice Depending Upon The Number Of Cards\n")
    FirstPlayerChoiceToBePlayed -= 1
    return FirstPlayerChoiceToBePlayed



def ResurrectSpellMode(OutDatedDeck):

    IndexOfCardToBePopped = random.randint(0,OutDatedDeck.CountOfCardsInDeck - 1)
    RandomCardFromOutDatedDeckPlayer = OutDatedDeck.AddCardInOutdatedDeck.pop(IndexOfCardToBePopped -1)   
    return RandomCardFromOutDatedDeckPlayer


def RoundOne():
    ChoiceOfPlay = input("\nEnter the Choice of Play 1. God Spell 2. Regular Mode\n")
    if ChoiceOfPlay == 1:

        CardNumberForSecondPlayer = GodSpellMode()
        RoundStartingPlayer.GodSpell = 0

        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[CardNumberForSecondPlayer - 1].CardStrength:

            RoundStartingPlayer.FirstPlayerScore += 1
            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(CardNumberForSecondPlayer - 1)
            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
            RoundStartingPlayer.PlayerOneFlag = "True"
            RoundSecondPlayer.PlayerTwoFlag = "False"

        else:

            RoundSecondPlayer.SecondPlayerScore += 1
            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(CardNumberForSecondPlayer - 1)
            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
            RoundStartingPlayer.PlayerOneFlag = "False"
            RoundSecondPlayer.PlayerTwoFlag = "True"

    else:

        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
            RoundStartingPlayer.FirstPlayerScore += 1
            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
            RoundStartingPlayer.PlayerOneFlag = "True"
            RoundSecondPlayer.PlayerTwoFlag = "False"

        else:
            RoundSecondPlayer.SecondPlayerScore += 1
            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
            RoundStartingPlayer.PlayerOneFlag = "False"
            RoundSecondPlayer.PlayerTwoFlag = "True"

def AfterFirstRound(RoundStartingPlayer,RoundSecondPlayer,OutDatedDeck): 
    while RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck !=0 or RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck != 0:

        if RoundStartingPlayer.PlayerOneFlag == "True" and RoundSecondPlayer.PlayerTwoFlag == "False":
            RoundStartingPlayer = FirstPlayer
            RoundSecondPlayer = SecondPlayer
        else:
            RoundStartingPlayer = SecondPlayer
            RoundSecondPlayer = FirstPlayer 

        if RoundStartingPlayer.GodSpell == 1 and RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck != 0 and RoundStartingPlayer.ResurrectSpell == 1:

            ChoiceOfPlay = input("\nEnter the Choice of Play 1. God Spell 2. Resurrect Mode 3. Regular Mode\n")

            if ChoiceOfPlay == 1 and RoundStartingPlayer.GodSpell == 1:
                RoundStartingPlayer.GodSpell = 0
                CardNumberForSecondPlayer = GodSpellMode()

                if RoundSecondPlayer.ResurrectSpell == 1 and OutDatedDeck.CountOfCardsInDeck != 0:

                    choice = raw_input("\nDoes the Looser Player Wants to Play Resurrect Spell Yes or No \n")

                    if choice == 'Yes':    

                           
                        ResurrectCardForSecondPlayer = ResurrectSpellMode(OutDatedDeck)
                        RoundSecondPlayer.PlayerDeck.AddCardIntoDeck(ResurrectCardForSecondPlayer)
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck += 1
                        print("\n\nIncreased Count of Cards\n\n")

                        print("\nDoes the Starting Player Wants to Play The Original God Spell Card or The New Resurrect Card\n")
                        
                        ChoiceForTheRound = raw_input("\nEnter Yes For God Spell Or No for Resurrect Spell\n")

                        if ChoiceForTheRound == 'Yes':

                            if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                                RoundStartingPlayer.FirstPlayerScore += 1
                                FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                                SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(CardNumberForSecondPlayer)
                                OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                                OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                                RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                                RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                                RoundStartingPlayer.PlayerOneFlag = "True"
                                RoundSecondPlayer.PlayerTwoFlag = "False"
                                
                            else:
                                RoundSecondPlayer.SecondPlayerScore += 1
                                FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                                SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(CardNumberForSecondPlayer -1)
                                OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                                OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                                RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                                RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                                RoundStartingPlayer.PlayerOneFlag = "False"
                                RoundSecondPlayer.PlayerTwoFlag = "True"
                        else:
                            RoundSecondPlayer.ResurrectSpell = 0 
                            if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                                RoundStartingPlayer.FirstPlayerScore += 1
                                FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                                SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                                OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                                OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                                RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                                RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                                RoundStartingPlayer.PlayerOneFlag = "True"
                                RoundSecondPlayer.PlayerTwoFlag = "False"
                            else:
                                RoundSecondPlayer.SecondPlayerScore += 1
                                FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                                SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                                OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                                OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                                RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                                RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                                RoundStartingPlayer.PlayerOneFlag = "False"
                                RoundSecondPlayer.PlayerTwoFlag = "True"
                    else:
                        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[CardNumberForSecondPlayer - 1].CardStrength:
                            RoundStartingPlayer.FirstPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(CardNumberForSecondPlayer - 1)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "True"
                            RoundSecondPlayer.PlayerTwoFlag = "False"

                        else:           
                            RoundSecondPlayer.SecondPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(CardNumberForSecondPlayer - 1)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "False"
                            RoundSecondPlayer.PlayerTwoFlag = "True"
                               
            elif ChoiceOfPlay == 2 and OutDatedDeck.CountOfCardsInDeck != 0:
                ResurrectCardForFirstPlayer = ResurrectSpellMode(OutDatedDeck)
                RoundStartingPlayer.PlayerDeck.AddCardIntoDeck(ResurrectCardForFirstPlayer)
                RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck += 1
                RoundStartingPlayer.ResurrectSpell = 0
                if RoundSecondPlayer.ResurrectSpell == 1 and OutDatedDeck.CountOfCardsInDeck >=1:
                    choice = raw_input("\nDoes the Looser Player Wants to Play Resurrect Spell Yes or No \n")      
                    if choice == 'Yes':
                        ResurrectCardForSecondPlayer = ResurrectSpellMode(OutDatedDeck)
                        RoundSecondPlayer.PlayerDeck.AddCardIntoDeck(ResurrectCardForSecondPlayer)
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck += 1
                        RoundSecondPlayer.ResurrectSpell = 0 
                        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                            RoundStartingPlayer.FirstPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "True"
                            RoundSecondPlayer.PlayerTwoFlag = "False"
                        else:
                            RoundSecondPlayer.SecondPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "False"
                            RoundSecondPlayer.PlayerTwoFlag = "True"
                    else:
                        RoundStartingPlayer.ResurrectSpell = 0
                        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                            RoundStartingPlayer.FirstPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1  
                            RoundStartingPlayer.PlayerOneFlag = "True"
                            RoundSecondPlayer.PlayerTwoFlag = "False"
                        else:
                            RoundSecondPlayer.SecondPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "False"
                            RoundSecondPlayer.PlayerTwoFlag = "True"
                else:
                    if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                        RoundStartingPlayer.FirstPlayerScore += 1
                        FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                        SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                        OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                        OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                        RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundStartingPlayer.ResurrectSpell = 0
                        RoundStartingPlayer.PlayerOneFlag = "True"
                        RoundSecondPlayer.PlayerTwoFlag = "False"
                    else:
                        RoundSecondPlayer.SecondPlayerScore += 1
                        FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                        SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                        OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                        OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                        RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundStartingPlayer.ResurrectSpell = 0
                        RoundStartingPlayer.PlayerOneFlag = "False"
                        RoundSecondPlayer.PlayerTwoFlag = "True" 

            elif ChoiceOfPlay == 3: 

                if RoundSecondPlayer.ResurrectSpell == 1 and OutDatedDeck.CountOfCardsInDeck != 0:
                 
                    choice = raw_input("\nDoes the Looser Player Wants to Play Resurrect Spell Yes or No \n")

                    if choice == 'Yes':

                        ResurrectCardForSecondPlayer = ResurrectSpellMode(OutDatedDeck)
                        RoundSecondPlayer.PlayerDeck.AddCardIntoDeck(ResurrectCardForSecondPlayer)
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck += 1
                        RoundSecondPlayer.ResurrectSpell = 0

                        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                            RoundStartingPlayer.FirstPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "True"
                            RoundSecondPlayer.PlayerTwoFlag = "False"

                        else:
                            RoundSecondPlayer.SecondPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "False"
                            RoundSecondPlayer.PlayerTwoFlag = "True"
                    
                    else:
                        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                            RoundStartingPlayer.FirstPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "True"
                            RoundSecondPlayer.PlayerTwoFlag = "False"

                        else:
                            RoundSecondPlayer.SecondPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "False"
                            RoundSecondPlayer.PlayerTwoFlag = "True"
                else:
                    if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                        RoundStartingPlayer.FirstPlayerScore += 1
                        FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                        SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                        OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                        OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                        RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundStartingPlayer.PlayerOneFlag = "True"
                        RoundSecondPlayer.PlayerTwoFlag = "False"

                    else:
                        RoundSecondPlayer.SecondPlayerScore += 1
                        FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                        SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                        OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                        OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                        RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundStartingPlayer.PlayerOneFlag = "False"
                        RoundSecondPlayer.PlayerTwoFlag = "True"
            else:
                print("\nWrong Choice\n")
                exit(300)
    
        elif RoundStartingPlayer.ResurrectSpell == 1 and OutDatedDeck.CountOfCardsInDeck != 0 and RoundStartingPlayer.GodSpell == 0:

            ChoiceOfPlay = input("\nEnter the Choice of Play 1. Resurrect Spell 2. Regular Mode ")

            if ChoiceOfPlay == 1:
                ResurrectCardForFirstPlayer = ResurrectSpellMode(OutDatedDeck)
                RoundStartingPlayer.PlayerDeck.AddCardIntoDeck(ResurrectCardForFirstPlayer)
                RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck += 1
                RoundStartingPlayer.ResurrectSpell = 0
        
                if RoundSecondPlayer.ResurrectSpell == 1 and OutDatedDeck.CountOfCardsInDeck >=1:

                    choice = raw_input("\nDoes the Looser Player Wants to Play Resurrect Spell Yes or No\n")

                    if choice == 'Yes':
                        
                        ResurrectCardForSecondPlayer = ResurrectSpellMode(OutDatedDeck)
                        RoundSecondPlayer.PlayerDeck.AddCardIntoDeck(ResurrectCardForSecondPlayer)
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck += 1
                        RoundSecondPlayer.ResurrectSpell = 0

                        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                            RoundStartingPlayer.FirstPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "True"
                            RoundSecondPlayer.PlayerTwoFlag = "False"
                            
                        else:
                            RoundSecondPlayer.SecondPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "False"
                            RoundSecondPlayer.PlayerTwoFlag = "True"

                        
                    else:
                        RoundSecondPlayer.ResurrectSpell = 0
                        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                            RoundStartingPlayer.FirstPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "True"
                            RoundSecondPlayer.PlayerTwoFlag = "False"
                            RoundStartingPlayer.ResurrectSpell = 0
                        else:
                            RoundSecondPlayer.SecondPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "False"
                            RoundSecondPlayer.PlayerTwoFlag = "True"   
                else:
                    RoundStartingPlayer.ResurrectSpell = 0
                    if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                        RoundStartingPlayer.FirstPlayerScore += 1
                        FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                        SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                        OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                        OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                        RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundStartingPlayer.PlayerOneFlag = "True"
                        RoundSecondPlayer.PlayerTwoFlag = "False"
                        
                    else:
                        RoundSecondPlayer.SecondPlayerScore += 1
                        FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                        SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                        OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                        OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                        RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                        RoundStartingPlayer.PlayerOneFlag = "False"
                        RoundSecondPlayer.PlayerTwoFlag = "True"
                        RoundStartingPlayer.ResurrectSpell = 0   
    
            else:

                if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                    RoundStartingPlayer.FirstPlayerScore += 1
                    FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                    SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                    OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                    OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                    RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundStartingPlayer.PlayerOneFlag = "True"
                    RoundSecondPlayer.PlayerTwoFlag = "False"

                else:
                    RoundSecondPlayer.SecondPlayerScore += 1
                    FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                    SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                    OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                    OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                    RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundStartingPlayer.PlayerOneFlag = "False"
                    RoundSecondPlayer.PlayerTwoFlag = "True"

        elif RoundStartingPlayer.ResurrectSpell == 0 and RoundStartingPlayer.GodSpell == 1:
            ChoiceOfPlay = input("\nEnter the Choice of Play 1. God Spell 2. Regular Mode\n")

            if ChoiceOfPlay == 1:

                RoundStartingPlayer.GodSpell = 0
                CardNumberForSecondPlayer = GodSpellMode()

                if RoundSecondPlayer.ResurrectSpell == 1 and OutDatedDeck.CountOfCardsInDeck != 0:
                    
                    choice = raw_input("\nDoes the Looser Player Wants to Play Resurrect Spell Yes or No\n")
                    if choice == 'Yes':
                        ResurrectCardForSecondPlayer = ResurrectSpellMode(OutDatedDeck)
                        RoundSecondPlayer.PlayerDeck.AddCardIntoDeck(ResurrectCardForSecondPlayer)
                        RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck += 1
                        RoundSecondPlayer.ResurrectSpell = 0

                        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                            RoundStartingPlayer.FirstPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "True"
                            RoundSecondPlayer.PlayerTwoFlag = "False"
                            
                        else:
                            RoundSecondPlayer.SecondPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "False"
                            RoundSecondPlayer.PlayerTwoFlag = "True"
                            
                    else:
                        if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[CardNumberForSecondPlayer - 1].CardStrength:
                            RoundStartingPlayer.FirstPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(CardNumberForSecondPlayer)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "True"
                            RoundSecondPlayer.PlayerTwoFlag = "False"
                        else:
                            RoundSecondPlayer.SecondPlayerScore += 1
                            FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                            SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(CardNumberForSecondPlayer - 1)
                            OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                            OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                            RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                            RoundStartingPlayer.PlayerOneFlag = "False"
                            RoundSecondPlayer.PlayerTwoFlag = "True"
            else:
                if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                    RoundStartingPlayer.FirstPlayerScore += 1
                    FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                    SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                    OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                    OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                    RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundStartingPlayer.PlayerOneFlag = "True"
                    RoundSecondPlayer.PlayerTwoFlag = "False"
                else:
                    RoundSecondPlayer.SecondPlayerScore += 1
                    FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                    SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                    OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                    OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                    RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundStartingPlayer.PlayerOneFlag = "False"
                    RoundSecondPlayer.PlayerTwoFlag = "True"
    

        elif RoundStartingPlayer.ResurrectSpell == 0 and RoundStartingPlayer.GodSpell == 0:
            if RoundSecondPlayer.ResurrectSpell == 1 and OutDatedDeck.CountOfCardsInDeck != 0:
                choice = raw_input("\nDoes the Looser Player Wants to Play Resurrect Spell Yes or No\n")
                ResurrectCardForSecondPlayer = ResurrectSpellMode(OutDatedDeck)
                RoundSecondPlayer.PlayerDeck.AddCardIntoDeck(ResurrectCardForSecondPlayer)
                RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck += 1
                RoundSecondPlayer.ResurrectSpell = 0

                if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                    RoundStartingPlayer.FirstPlayerScore += 1
                    FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                    SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                    OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                    OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                    RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundStartingPlayer.PlayerOneFlag = "True"
                    RoundSecondPlayer.PlayerTwoFlag = "False"
                       
                else:
                    RoundSecondPlayer.SecondPlayerScore += 1
                    FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                    SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                    OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                    OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                    RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundStartingPlayer.PlayerOneFlag = "False"
                    RoundSecondPlayer.PlayerTwoFlag = "True"
            else:

                if RoundStartingPlayer.PlayerDeck.CardInDeck[0].CardStrength > RoundSecondPlayer.PlayerDeck.CardInDeck[0].CardStrength:
                    RoundStartingPlayer.FirstPlayerScore += 1
                    FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                    SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                    OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                    OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                    RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundStartingPlayer.PlayerOneFlag = "True"
                    RoundSecondPlayer.PlayerTwoFlag = "False"

                else:
                    RoundSecondPlayer.SecondPlayerScore += 1
                    FirstPlayerCardDeleted = RoundStartingPlayer.PlayerDeck.CardInDeck.pop(0)
                    SecondPlayerCardDeleted = RoundSecondPlayer.PlayerDeck.CardInDeck.pop(0)
                    OutDatedDeck.OutDatedListFormation(FirstPlayerCardDeleted)
                    OutDatedDeck.OutDatedListFormation(SecondPlayerCardDeleted)
                    RoundStartingPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundSecondPlayer.PlayerDeck.CountOfCardsInDeck -= 1
                    RoundStartingPlayer.PlayerOneFlag = "False"
                    RoundSecondPlayer.PlayerTwoFlag = "True"
            


RoundOne()
OutDatedDeck.ShowOutDatedDeck()
print("\nPlayer One Score = ", RoundStartingPlayer.FirstPlayerScore)
print("\nPlayer Two Score = ", RoundSecondPlayer.SecondPlayerScore)

if RoundStartingPlayer.PlayerOneFlag == "True" and RoundSecondPlayer.PlayerTwoFlag == "False":
            RoundStartingPlayer = FirstPlayer
            RoundSecondPlayer = SecondPlayer
else:
    RoundStartingPlayer = SecondPlayer
    RoundSecondPlayer = FirstPlayer 

AfterFirstRound(RoundStartingPlayer,RoundSecondPlayer,OutDatedDeck)    

if RoundStartingPlayer.PlayerOneFlag == "True":
    print("\n\nWinner is ",RoundStartingPlayer.PlayerName)
else:
    print("\n\nWinner is",RoundSecondPlayer.PlayerName)





   
        







