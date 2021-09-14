import unittest
import decoraters

class Test(unittest.TestCase):
    def test(self):
        output = decoraters.add_all(1,2,3,4,5)
        self.assertEqual(output, 15)
if __name__ == '__main__':
    unittest.main()