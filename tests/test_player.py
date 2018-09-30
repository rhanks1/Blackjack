from player import Player
from pydealer import Card, Stack
import unittest

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_initial_chips(self):
        self.assertEqual(self.player.chips, 100)

    def test_initial_hand(self):
        self.assertEqual(self.player.hand.size, 0)

    def test_get_chips(self):
        self.player.chips = 26
        self.assertEqual(self.player.get_chips(), 26)

    def test_get_hand(self):
        card_1 = Card('Ace', 'Spades')
        card_2 = Card('2', 'Diamonds')
        temp_hand = [card_1, card_2]
        test_hand = Stack(cards=temp_hand)
        self.player.hand = test_hand
        self.assertEqual(self.player.get_hand(), test_hand)

    def test_empty_hand(self):
        card_1 = Card('Ace', 'Spades')
        card_2 = Card('2', 'Diamonds')
        temp_hand = [card_1, card_2]
        test_hand = Stack(cards=temp_hand)
        self.player.hand = test_hand
        self.player.empty_hand()
        self.assertEqual(self.player.hand.size, 0)
        # Test that emptying an empty hand is ok
        self.player.empty_hand()
        self.assertEqual(self.player.hand.size, 0)

    def test_add_cards(self):
        card_1 = Card('Jack', 'Clubs')
        card_2 = Card('King', 'Hearts')
        temp_hand = [card_1]
        test_hand = Stack(cards=temp_hand)
        self.player.add_cards(temp_hand)
        self.assertEqual(self.player.hand, test_hand)
        # Test adding the same card twice
        self.player.add_cards(temp_hand)
        temp_hand = [card_1, card_1]
        test_hand = Stack(cards=temp_hand)
        self.assertEqual(self.player.hand, test_hand)
        temp_hand = [card_2]
        self.player.add_cards(temp_hand)
        temp_hand = [card_1, card_1, card_2]
        test_hand = Stack(cards=temp_hand)
        self.assertEqual(self.player.hand, test_hand)

    def test_add_chips(self):
        self.player.add_chips(100)
        self.assertEqual(self.player.chips, 200)
        self.player.add_chips(-100)
        self.assertEqual(self.player.chips, 100)
        self.player.add_chips(26)
        self.assertEqual(self.player.chips, 126)

    def take_chips(self):
        self.player.take_chips(50)
        self.assertEqual(self.player.chips, 50)
        self.player.take_chips(24)
        self.assertEqual(self.player.chips, 26)


        

if __name__ =='__main__':
    unittest.main()
