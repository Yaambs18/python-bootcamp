import unittest
from card_deck_class import Deck

class Test_deck(unittest.TestCase):
    def test_count(self):
        obj = Deck()
        result = obj.count
        self.assertEqual(result, 52)

if __name__ == '__main__':
    unittest.main()