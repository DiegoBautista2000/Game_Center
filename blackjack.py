# Alex Melo, Diego Bautista COP1047C-2227-8751|Introduction to Python Program
# Group Project
# Random library for deck
import random

# Card's suits, ranks and values

suits = ('♥', '♦', '♠', '♣')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}


playing = True

############# Card Class will generate a card with the given suit and rank ################

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


############## Hand Class which will add the cards from deck class to the player's hand #############

class Hand:
    def __init__(self):
        self.cards = []  # Start with an empty list as we did in the Deck class
        self.value = 0   # Start with zero value
        self.aces = 0    # Add an attribute to keep track of aces

############### Add_card function will add a card to the player's hand ##############

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

############### Ace can have two values 1 or 11, ace_value will adjust the value of ace


    def ace_values(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

###############  Chips class keeps track of the Player's starting chip count, and calculates their bets, plus ongoing chip count depending on wins and loses. ###############

class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def bet_won(self):
        self.total += self.bet

    def bet_lost(self):
        self.total -= self.bet


############## FUNCTIONS #############


############## FUNCTION FOR TAKING BETS #############
def place_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? (Maximum chip bet is 100):'))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Your bet cannot exceed",chips.total)
            else:
                break

############## Function for taking hits #############

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.ace_values()

############## Function prompting the Player to Hit or Stand #############

def hit_or_stand(deck,hand):
    global playing  # Loop control for when player hits or stands

    while True:
        try:
            x = input("Would you like to Hit or Stand? Type 'h' for Hit or 's' for Stand. Hit Enter once choice is selected: ")
        except ValueError:
            print("Please enter 'h' or 's'")
        if x[0].lower() == 'h':
            hit(deck,hand)  # Refers to hit function on line 108-111

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


############## Functions to display cards #############

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value, '\n')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value, '\n')


############## Functions to handle end of game scenarios #############

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.bet_lost()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.bet_won()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.bet_won()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.bet_lost()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

############## Blackjack Game #############

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until they reach 18. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100

    # Prompt the Player for their bet
    place_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break


            # If Player hasn't busted, play Dealer's hand until Dealer reaches 18
    if player_hand.value <= 21:

        while dealer_hand.value < 18:
            hit(deck,dealer_hand)

            # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

            # Inform Player of their chips total
    print("\nCurrent total chip count stands at",player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break