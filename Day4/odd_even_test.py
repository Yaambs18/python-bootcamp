import unittest
import odd_even

class Test_num(unittest.TestCase):
    def test_odd_even(self):
        result = odd_even.odd_even(7)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
