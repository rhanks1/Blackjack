# -*- coding: utf-8 -*-
"""
@author: learn
"""

BJ_RANKS = {
        'Ace': 11,
        'King': 10,
        'Queen': 10,
        'Jack': 10,
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

def get_hand_total(hand):
    """Returns the total of a hand. If there are Aces in the hand and
    the total of the hand is greater than 21, the function will count
    as many Aces low as it takes to keep the toal under 21. """
    total = 0
    aces = 0
    for card in hand:
        if card.value == "Ace":
            aces += 1
        total += BJ_RANKS[card.value]
    if total > 21:
        for i in range(aces):
            if (total - 10 * (i+1)) <= 21:
                return total - 10 * (i+1)
    return total

def check_for_bust(hand):
    """Returns True if the total of a hand is more than 21, False otherwise."""
    total = get_hand_total(hand)
    if total > 21:
        return True

def check_for_blackjack(hand):
    """Returns True if the hand is a blackjack, False otherwise."""
    total = get_hand_total(hand)
    if total == 21:
        return True
    return False
