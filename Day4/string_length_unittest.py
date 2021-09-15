import unittest
import count

class Test_Count(unittest.TestCase):
    def test_strlength(self):
        name = "Yansh Bhardwaj"
        length = count.char_count(name)
        self.assertEqual(length, len(name))

if __name__ == '__main__':
    unittest.main()