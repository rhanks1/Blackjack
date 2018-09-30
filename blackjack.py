# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:27:43 2018

@author: Ryan Hanks
"""

import math
from functions import get_hand_total, check_for_bust, check_for_blackjack, \
	BJ_RANKS
from pydealer import Stack
from dealer import Dealer
from player import Player

SUITS = {'Spades': '♠','Hearts': '♥','Diamonds': '♦','Clubs': '♣'}
VALUES = {
        'Ace': 'A',
        'King': 'K',
        'Queen': 'Q',
        'Jack': 'J',
    }

class GameManager(object):
    STARTING_CHIPS = 100
    
    def __init__(self):
        self.dealer = Dealer()
        self.quit = False
        self.user = Player()
        
    def setup(self):
        print("\n")
        print("WELCOME TO BLACKJACK!\n")   
        print("You will start with 100 chips")
        print("Blackjack pays out 3:2.")
        print("Double Down and Split bets can be less than or equal " +\
			"to original bet.")
        print("Only one card will be dealt to Double Down and Split hands.")
        print("No insurance will be offered.")
        print("Have Fun!\n\n\n")
        
    def ask_to_quit(self):
        """Check if the user wants to quit the game"""
        if self.user.get_chips() == 0:
            print("Game Over, you have 0 chips remaining.")
            self.quit = True
            return True
        user_input = input("Enter 'C' to continue or 'Q' to quit.\n")
        while user_input != 'C' and user_input != 'Q':
            user_input = input("Invalid input, enter 'C' to coninue " +\
				"or 'Q' to quit.\n")
        if user_input == 'Q':
            self.quit = True
            return True
        return False
            
    def get_bet(self):
        """Get a bet from the user through the command line"""
        user_input = input("Enter integer ammount to bet.\n")
        while True:
            try:
                bet = int(user_input)
                assert(bet > 0 and bet <= self.user.get_chips())
                return bet
            except ValueError:
                print("Bet must be an Integer.")
            except AssertionError:
                print("Valid bets are greater than 0 and less than {} chips."\
					.format(self.user.get_chips()))
            user_input = input("Enter integer ammount to bet.\n")
            
    def play_hand(self, bet):
        """Logic for playing a hand of Blackjack is contained in this mehod"""
        # Deal two cards to the user and the dealer
        self.dealer.initial_deal(self.user)
        self.display_table(self.user.get_hand(), bet, self.user.get_chips())
        # Check if either hand is a blackjack and payout accordingly
        dealer_bj = check_for_blackjack(self.dealer.get_hand())
        user_bj = check_for_blackjack(self.user.get_hand())
        if dealer_bj and user_bj:
            print("Push")
            print("Current chip total is {}.".format(self.user.get_chips()))
            return
        elif dealer_bj:
            self.user.take_chips(bet)
            self.display_table(self.user.get_hand(), bet,
                self.user.get_chips(), hide_dealer=False)
            print("Dealer has Blackjack. You lose.")
            print("Current chip total is {}.".format(self.user.get_chips()))
            return
        elif user_bj:
            payout = bet * 1.5
            self.user.add_chips(math.ceil(payout))
            print("Black Jack!")
            print("Current chip total is {}.".format(self.user.get_chips()))
            return  
        # Ask the user to Hit, Stand, Double Down, or Split
        choice = self.user_choice(bet)
        if choice == 'H':
            while choice != 'S':
                self.user.add_cards(self.dealer.deal())
                self.display_table(self.user.get_hand(), bet,
                    self.user.get_chips()) 
                if check_for_bust(self.user.get_hand()): 
                    self.user.take_chips(bet)
                    print("BUST")
                    print("Current chip total is {}."\
						.format(self.user.get_chips()))
                    return
                choice = input("'H' to hit, 'S' to stand.\n")
                while choice != 'H' and choice != 'S':
                    choice = input("Invalid input, please select 'H' to hit, "\
						"'S' to stand.\n")
        elif choice == 'D':
            double_down = self.get_bet()
            while double_down > bet or double_down > \
				self.user.get_chips() - bet:
                if double_down > self.user.get_chips() - bet:
                    print("Double down bet can't be greater than " +\
						"your remiaining chips.")
                else:
                    print("Double down bet must be less than or equal " +\
						"to original bet.")
                double_down = self.get_bet()
            bet += double_down
            self.user.add_cards(self.dealer.deal())
            if check_for_bust(self.user.get_hand()):
                self.display_table(self.user.get_hand(), bet,
                    self.user.get_chips(), hide_dealer=False)
                self.user.take_chips(bet)
                print("BUST")
                print("Current chip total is {}.".format(self.user.get_chips()))
                return
        elif choice == 'P':
            split_bet = self.get_bet()
            while split_bet > bet or split_bet > self.user.get_chips() - bet:
                if split_bet > self.user.get_chips() - bet:
                    print("Split bet can't be greater than your " +\
						"remiaining chips.")
                else:
                    print("Split bet must be less than or equal to " +\
						"original bet.")
                split_bet = self.get_bet()
            bet_total = bet + split_bet
            hand_1 = Stack()
            hand_2 = Stack()
            hand_1 += self.user.get_hand().deal(1)
            hand_1 += self.dealer.deal()
            hand_2 += self.user.get_hand().deal(1)
            hand_2 += self.dealer.deal()
            if get_hand_total(self.dealer.get_hand()) < 17:
                self.display_table(hand_1, bet_total, 
                    self.user.get_chips())
                self.display_table(hand_2, bet_total,
                    self.user.get_chips())
            else:
                self.display_table(hand_1, bet_total,
                    self.user.get_chips(), hide_dealer=False)
                self.display_table(hand_2, bet_total, 
                    self.user.get_chips(), hide_dealer=False)
            while get_hand_total(self.dealer.get_hand()) < 17:
                self.dealer.deal_dealer()
                self.display_table(hand_1, bet_total, 
                    self.user.get_chips(), hide_dealer=False)
                self.display_table(hand_2, bet_total, 
                    self.user.get_chips(), hide_dealer=False)
            if check_for_bust(self.dealer.get_hand()):
                self.user.add_chips(bet)
                self.user.add_chips(split_bet)
                print("DEALER BUSTS, YOU WIN!")
                print("Current chip total is {}.".format(self.user.get_chips()))
                return
            self.compare_hands(bet,hand_1)        
            self.compare_hands(split_bet, hand_2)
            return
        if choice != 'P':
            self.display_table(self.user.get_hand(), bet,
                self.user.get_chips(), hide_dealer=False)
        while get_hand_total(self.dealer.get_hand()) < 17:
            self.dealer.deal_dealer()
            self.display_table(self.user.get_hand(), bet,
                self.user.get_chips(), hide_dealer=False)
        if check_for_bust(self.dealer.get_hand()):
            self.user.add_chips(bet)
            print("DEALER BUSTS, YOU WIN!")
            print("Current chip total is {}.".format(self.user.get_chips()))
            return
        # If neither hand has busted, check which hand is higher and settle bet
        self.compare_hands(bet, self.user.get_hand())
            
    def clean_up_hand(self):
        """Clean up after hand is over"""
        self.dealer.empty_hand()
        self.user.empty_hand()
        if len(self.dealer.deck) < self.dealer.cut_num:
            self.dealer.reshuffle()
        
            
    def compare_hands(self, bet, user_hand):
        """Compare hands to see which hand wins. An assumption this method 
        makes is that both hands are under 21."""
        dealer_total = get_hand_total(self.dealer.get_hand())
        user_total = get_hand_total(user_hand)
        if dealer_total == user_total:
            print("Push")
            print("Current chip total is {}.".format(self.user.get_chips()))
        elif dealer_total > user_total:
            self.user.take_chips(bet)
            print("House wins")
            print("Current chip total is {}.".format(self.user.get_chips()))
        else:
            self.user.add_chips(bet)
            print("Winner!")
            print("Current chip total is {}.".format(self.user.get_chips()))
        
    def display_table(self, hand, bet, chips_left, hide_dealer=True):
        """Display the current state of the table"""
        dealer_cards = []
        user_cards = []
        print("#################################")
        print("     POT: {:<3}   | CHIPS LEFT: {:<3}".format(bet, chips_left - bet))
        print("---------------------------------")
        print("  DEALER HAND   |   PLAYER HAND  ")
        for card in self.dealer.get_hand():
            dealer_cards.append(self.card_to_print(card, hide_dealer))
            hide_dealer = False
        for card in hand:
            user_cards.append(self.card_to_print(card))
        difference = self.dealer.get_hand().size - hand.size
        if difference < 0:
            for i in range(difference * -1):
                dealer_cards.append(self.card_to_print(place_holder=True))
        elif difference > 0:
            for i in range(difference):
                user_cards.append(self.card_to_print(place_holder=True))
        for i in range(max(len(dealer_cards), len(user_cards))):
            for j in range(7):
                print("{} | {}".format(dealer_cards[i][j], user_cards[i][j]))
         
    def card_to_print(self,card=None, hide_dealer=False, place_holder=False):
        """Returs a printable representation of a playing card."""
        lines = []
        if place_holder:
            lines.append('               ')
            lines.append('               ')
            lines.append('               ')
            lines.append('               ')
            lines.append('               ')
            lines.append('               ')
            lines.append('               ')
            return lines
        suit = SUITS[card.suit]
        if card.value in VALUES:
            value = VALUES[card.value]
        else:
            value = card.value
        if hide_dealer:
            lines.append('   ┌───────┐   ')
            lines.append('   |*******|   ')
            lines.append('   |*******|   ')
            lines.append('   |*******|   ')
            lines.append('   |*******|   ')
            lines.append('   |*******|   ')
            lines.append('   └───────┘   ')
            return lines
            
        else:
            suit = SUITS[card.suit]
            if card.value in VALUES:
                value = VALUES[card.value]
            else:
                value = card.value
            lines.append('   ┌───────┐   ')
            lines.append('   | {:<2}    |   '.format(value))
            lines.append('   |       |   ')
            lines.append('   |   {}   |   '.format(suit))
            lines.append('   |       |   ')
            lines.append('   |    {:>2} |   '.format(value))
            lines.append('   └───────┘   ')
            return lines

    def user_choice(self, bet):
        """Collect a choice from the user through the command line"""
        choice = ''
        while choice != 'H' and choice != 'S' and choice != 'D' \
			and choice != 'P':
            choice = input("Please select 'H' to hit, 'S' to stand, 'D' " + \
				"to double-down, or 'P' to split.\n")
            if choice == 'D' and self.user.get_chips() - bet == 0:
                choice = ''
                print("Invalid choice, you have no additional chips to bet.")
            if choice == 'P' and self.user.get_chips() - bet == 0:
                choice = ''
                print("Invalid choice, you have no additional chips to bet.")
            elif choice == 'P':
                user_hand = self.user.get_hand()
                card_list = []
                for card in user_hand:
                    card_list.append(card)
                if BJ_RANKS[card_list[0].value] != BJ_RANKS[card_list[1].value]:
                    print("Invalid choice, you must have a pair to split.")
                    choice = ''  
        return choice
    
    def run(self):
        """Run loop for the game manager"""
        self.setup()
        while not self.quit:
            if not self.ask_to_quit():
                bet = self.get_bet()
                self.play_hand(bet)
                self.clean_up_hand()
        self.teardown()
            
    def teardown(self):
        """Preform necessary teardown at the end of the game."""
        if self.user.chips >= 100:
            print("Congratulations you won {} dollars!".format(
                    self.user.get_chips() - 100))
        else:
            print("Better luck next time.")
    
        
if __name__ == '__main__':
    game = GameManager()
    game.run()
    
