# CARD GAME
# STEP1: import random and gloabal variable.
# --> import the random module.this will be used to shuffle the deck or prior to dealing.
#--> then declare the variable to store the suits,rank and values.
# --->suits=('hearts',"dimonds","spades","clubs")
# ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
# values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}

import random
suits=('hearts',"dimonds","spades","clubs")
ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}
playing=True

# STEP 2: CREATE A CARD CLASS
#---> a card object need only two attributes SUIT AND RANK.
#--> In addition to the cards __init__ method,consider a adding a __str__ method that we can asked to print a card,returns the strings in the form of two heart.

class card():
    def __int__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.suits + 'of' +self.rank

# STEP 3: create a desk class:
# here we migght store 52 card objects in a list that can latter be shuffled.

class deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))


