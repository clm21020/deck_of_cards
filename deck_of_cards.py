import random

def pick_suit (number):
    suit = ["Spades", "Diamonds", "Clubs", "Hearts"]
    return suit[number]

def pick_rank (number):
    """
    """
    rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    return rank[number]

def new_deck():
    key = 0
    deck = {}
    for i in xrange(0, 4):
        suit = pick_suit(i)
        for j in xrange(0,13):
            rank = pick_rank(j)
            deck[str(key)] = (rank + " of " + suit)
            key += 1
    return deck

def prompt_user():
    number_of_cards = raw_input("How many cards would you like to be dealt? ")
    return int(number_of_cards)

def random_card():
    rando = random.randint(0, 51)
    return str(rando)


deck = new_deck()

while(True):
    number_of_cards = prompt_user()
    for i in xrange(0, number_of_cards): 
        print(deck[random_card()])


    """
    Return list of suits
    @number: 
    any extra stuff
    """