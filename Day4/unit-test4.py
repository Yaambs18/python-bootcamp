import unittest
import line_class

class TestCap(unittest.TestCase):
    def test_distance(self):
        coordinate1 = (3,2)
        coordinate2 = (8,10)
        obj = line_class.Line(coordinate1,coordinate2)
        result = obj.distance()
        self.assertEqual(result, 9.433981132056603)
    
    def test_slope(self):
        coordinate1 = (3,2)
        coordinate2 = (8,10)
        obj = line_class.Line(coordinate1,coordinate2)
        result = obj.slope()
        self.assertEqual(result, 1.6) 

if __name__ == '__main__':
    unittest.main()