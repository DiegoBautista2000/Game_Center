# WELCOME TO BLACKJACK GAME CODE, IF YOU HAVE NO IDEA WHAT IS A BLACKJACK GAME

# Random library
import random

# Card's suits, ranks and values

suits = ('Heart', 'Diamond', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}


playing = True

############# Card Class will initiate a card with the given suit and rank ################

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


############## Following below is the Deck Class which will create a deck from the given cards #############

class Deck:

    def __init__(self):
        self.deck = []  # Start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # Build Card objects and add them to the list

    def __str__(self):
        deck_comp = ''  # Start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # Add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):          # Shuffle function will shuffle the whole deck
        random.shuffle(self.deck)

    def deal(self):             # Deal function will take one card from the deck
        single_card = self.deck.pop()
        return single_card