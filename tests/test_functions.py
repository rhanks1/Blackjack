from player import Player
from functions import get_hand_total, check_for_bust, check_for_blackjack

from pydealer import Card, Stack

import unittest

class TestFunctions(unittest.TestCase):
    def test_check_for_blackjack(self):
        card_1 = Card('Ace', 'Hearts')
        card_2 = Card('King', 'Spades')
        temp_hand = [card_1, card_2]
        test_hand_1 = Stack(cards=temp_hand)
        card_3 = Card('Ace', 'Hearts')
        card_4 = Card('Ace', 'Spades')
        temp_hand = [card_3, card_4]
        test_hand_2 = Stack(cards=temp_hand)
        card_5 = Card('10', 'Diamonds')
        card_6 = Card('Ace', 'Clubs')
        temp_hand = [card_5, card_6]
        test_hand_3 = Stack(cards=temp_hand)
        card_7 = Card('6', 'Hearts')
        card_8 = Card('5', 'Spades')
        temp_hand = [card_7, card_8]
        test_hand_4 = Stack(cards=temp_hand)
        self.assertTrue(check_for_blackjack(test_hand_1))
        self.assertFalse(check_for_blackjack(test_hand_2))
        self.assertTrue(check_for_blackjack(test_hand_3))
        self.assertFalse(check_for_blackjack(test_hand_4))

    def test_get_hand_total(self):
        card_1 = Card('Ace', 'Hearts')
        card_2 = Card('King', 'Spades')
        card_3 = Card('Ace', 'Hearts')
        card_4 = Card('Ace', 'Spades')
        card_5 = Card('10', 'Diamonds')
        card_6 = Card('Ace', 'Clubs')
        card_7 = Card('7', 'Hearts')
        card_8 = Card('9', 'Spades')
        card_9 = Card('Queen', 'Diamonds')
        temp_hand = [card_1, card_3, card_4]
        test_hand_1 = Stack(cards=temp_hand)
        temp_hand = [card_1, card_3, card_4, card_6]
        test_hand_2 = Stack(cards=temp_hand)
        temp_hand = [card_1, card_2, card_3, card_8]
        test_hand_3 = Stack(cards=temp_hand)
        temp_hand = [card_7, card_8, card_5]
        test_hand_4 = Stack(cards=temp_hand)
        temp_hand = [card_9, card_2]
        test_hand_5 = Stack(cards=temp_hand)
        self.assertEqual(get_hand_total(test_hand_1), 13)
        self.assertEqual(get_hand_total(test_hand_2), 14)
        self.assertEqual(get_hand_total(test_hand_3), 21)
        self.assertEqual(get_hand_total(test_hand_4), 26)
        self.assertEqual(get_hand_total(test_hand_5), 20)

    def test_check_for_bust(self):
        card_1 = Card('Ace', 'Hearts')
        card_2 = Card('2', 'Spades')
        card_3 = Card('Ace', 'Hearts')
        card_4 = Card('Jack', 'Spades')
        card_5 = Card('9', 'Diamonds')
        temp_hand = [card_1, card_3, card_4]
        test_hand_1 = Stack(cards=temp_hand)
        temp_hand = [card_1, card_3, card_4, card_5]
        test_hand_2 = Stack(cards=temp_hand)
        temp_hand = [card_1, card_2, card_3, card_5]
        test_hand_3 = Stack(cards=temp_hand)
        temp_hand = [card_2, card_3, card_4]
        test_hand_4 = Stack(cards=temp_hand)
        temp_hand = [card_2, card_3, card_4, card_5]
        test_hand_5 = Stack(cards=temp_hand)
        self.assertFalse(check_for_bust(test_hand_1))
        self.assertFalse(check_for_bust(test_hand_2))
        self.assertFalse(check_for_bust(test_hand_3))
        self.assertFalse(check_for_bust(test_hand_4))
        self.assertTrue(check_for_bust(test_hand_5))



        

if __name__ =='__main__':
    unittest.main()
