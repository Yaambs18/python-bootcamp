import unittest
from roman_class import Roman

class Test_roman(unittest.TestCase):
    def test_int_value(self):
        obj = Roman()
        result = obj.roman_to_int("IX")
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()
