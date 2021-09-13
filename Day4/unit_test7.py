import unittest
import greatest_func

class TestGreatest(unittest.TestCase):
    def test_greatest_num(self):
        a = 92
        b = 459
        c = 28
        largest = greatest_func.greatest(a,b,c)
        self.assertEqual(largest, 459)

if __name__ == '__main__':
    unittest.main()