# -*- coding: utf-8 -*-
"""
@author: Ryan Hanks
"""

import random
from pydealer import Deck, Stack

class Dealer(object):
    
    def __init__(self):
        self.deck = Deck()
        self.hand = Stack()
        self.deck.build()
        self.deck.shuffle()
        self.cut_num = random.randint(12, 42)
        
    def get_deck(self):
        return self.deck
    
    def get_hand(self):
        return self.hand
        
    def initial_deal(self, player):
        """Deal two cards to the player and the dealer."""
        cards = self.deck.deal(2)
        player.add_cards(cards)
        self.hand += self.deck.deal(2)
         
    def deal(self):
        """Get one card from the deck"""
        return self.deck.deal(1)

    def deal_dealer(self):
        """Deal one card to the dealer's hand"""
        self.hand += self.deck.deal(1)
        
    def empty_hand(self):
        """Remove all cards from the dealer's hand"""
        self.hand.empty()
    
    def reshuffle(self):
        """Reset the decks so that there is one deck of 104 shuffled cards"""
        print("Reshuffle")
        new_deck = Deck()
        new_deck.build()
        new_deck.shuffle()
        self.deck = new_deck()
        self.cut_num = random.randint(12, 42)
