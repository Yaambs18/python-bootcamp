import unittest
from temp_class import Temprature

class Test_temp(unittest.TestCase):
    def test_temp(self):
        obj = Temprature()
        result = obj.convertCelsius(32)
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()
