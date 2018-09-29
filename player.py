# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 00:29:37 2018

@author: learn
"""
from pydealer import Stack

class Player(object):
    
    def __init__(self, starting_chips=100):
        self.chips = starting_chips
        self.hand = Stack()
        
    def get_chips(self):
        return self.chips
    
    def get_hand(self):
        return self.hand
    
    def empty_hand(self):
        """Empties the contents of the player's hand"""
        self.hand.empty()
    
    def add_cards(self, cards):
        """Add the list of cards to the player's hand"""
        self.hand += cards
            
    def add_chips(self, num_chips):
        """Add chips to player's chip total"""
        self.chips += num_chips
    
    def take_chips(self, num_chips):
        """Subtract chips from player's chip total"""
        assert(num_chips <= self.chips)
        self.chips -= num_chips