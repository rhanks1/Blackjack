from dealer import Dealer
from player import Player
from pydealer import Card, Stack
import unittest

class TestDealer(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer()
        self.player = Player()

    def test_initial_deck_size(self):
        self.assertEqual(self.dealer.deck.size, 104)

    def test_cut_number(self):
        self.assertTrue(self.dealer.cut_num >= 12 and self.dealer.cut_num < 42)

    def test_get_deck(self):
        self.assertEqual(self.dealer.get_deck(), self.dealer.deck)

    def test_get_hand(self):
        card_1 = Card('Ace', 'Spades')
        card_2 = Card('2', 'Diamonds')
        temp_hand = [card_1, card_2]
        test_hand = Stack(cards=temp_hand)
        self.dealer.hand = test_hand
        self.assertEqual(self.dealer.get_hand(), test_hand)

    def test_initial_deal(self):
        self.dealer.initial_deal(self.player)
        self.assertEqual(self.dealer.deck.size, 100)
        self.assertEqual(self.dealer.hand.size, 2)
        self.assertEqual(self.player.hand.size, 2)

    def test_deal(self):
        # dealt cards are actually passed as a Stack
        card = self.dealer.deal()
        self.assertTrue(type(card) is Stack)
        self.assertEqual(card.size, 1)
        self.assertEqual(self.dealer.deck.size, 103)
     
    def test_deal_dealer(self):
        self.dealer.deal_dealer()
        self.assertEqual(self.dealer.hand.size, 1)
        self.assertEqual(self.dealer.deck.size, 103)
        self.dealer.deal_dealer()
        self.assertEqual(self.dealer.hand.size, 2)
        self.assertEqual(self.dealer.deck.size, 102)
        self.dealer.deal_dealer()
        self.assertEqual(self.dealer.hand.size, 3)
        self.assertEqual(self.dealer.deck.size, 101)

    def test_reshuffle(self):
        self.dealer.deal_dealer()
        self.dealer.deal_dealer()
        self.dealer.deal_dealer()
        self.dealer.deal_dealer()
        self.dealer.deal_dealer()
        self.assertEqual(self.dealer.deck.size, 99)
        self.dealer.reshuffle()
        self.assertEqual(self.dealer.deck.size, 104)

if __name__ =='__main__':
    unittest.main()
