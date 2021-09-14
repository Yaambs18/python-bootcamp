import unittest
import ar_circle

class Test_area(unittest.TestCase):
    def test_circle_area(self):
        result = ar_circle.area(7)
        result2 = ar_circle.area(10)
        self.assertEqual(result, 153.86)
        self.assertEqual(result2, 314.0)

if __name__ == '__main__':
    unittest.main()