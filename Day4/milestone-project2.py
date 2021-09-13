import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has : "+ deck_comp
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank]     

        if card.rank == 'Ace':
            self.aces+=1   

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -=10
            self.aces -=1

class Chip:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would u like to bet? "))
        except:
            print("Please provide an integer value.")
        else:
            if chips.bet > chips.total:
                print(f"You dont have enough chips, You have only {chips.total}")
            else:
                break

def hit(deck, hand):
    
    single_card = deck.deal()
    hand.add_cards(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s ")
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print("Player stands, Dealer's Turn")
            playing = False
        else:
            print("Please enter h or s only")
            continue
        break

def show_some(player, dealer):
    print("\n Dealer' hand: ")
    print("First card Hidden! ")
    print(dealer.cards[1])

    print("\n Player's hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):

    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of dealer's hand : {dealer.value}")

    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand : {player.value}")
    
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")