import unittest
import laptop_class

class TestCap(unittest.TestCase):

    def test_discount(self):
        ob1 = laptop_class.Laptop('dell', 'e7240', 45000)
        ob2 = laptop_class.Laptop('hp', 'axus', 55000)
        result1 = ob1.apply_discount(40)
        result2 = ob2.apply_discount(50)
        self.assertEqual(int(result1), 27000)
        self.assertEqual(int(result2), 27500)

if __name__ == '__main__':
    unittest.main()