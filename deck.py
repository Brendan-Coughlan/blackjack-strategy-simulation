import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if rank in ["J", "Q", "K"]:
            self.value = 10
        elif rank == "A":
            self.value = 11
        else:
            self.value = int(self.rank)

    def __str__(self):
        return f"{self.suit} {self.rank} {self.value}"


def populate_deck(num_decks=1):
    deck = []
    suits = ["♥", "♦", "♠", "♣"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for i in range(num_decks):
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit, rank))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_hand(deck, num_cards=1):
    hand = []
    for i in range(num_cards):
        hand.append(deck.pop())
    return hand

def calculate_hand_value(hand):
    total_value = 0
    ace = 0

    for card in hand:
        if card.rank == "A":
            ace += 1
        total_value += card.value

    while total_value > 21 and ace > 0:
        total_value -= 10
        ace -= 1

    return total_value
