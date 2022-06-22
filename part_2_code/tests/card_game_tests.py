import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("heart", 1)
        self.card2 = Card("dimond" , 4) 
        cards = [self.card1 , self.card2]

        self.cardgame = CardGame(cards)

    def test_check_for_ace(self):
        self.assertEqual(True,self.cardgame.check_for_ace(self.card1)) 


    def test_highest_card(self):
        self.assertEqual(self.card2 , self.cardgame.highest_card(self.card1,self.card2))  


    def test_cards_total(self):
        self.assertEqual("You have a total of 5" , self.cardgame.cards_total(self.cardgame))      

