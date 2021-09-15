import unittest
import palindrome_func

class TestPalindrome(unittest.TestCase):
    def test_boolean(self):
        name = "naman"
        result = palindrome_func.is_palindrome(name)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()