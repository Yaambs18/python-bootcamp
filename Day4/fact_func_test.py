import unittest
import fact_func

class Test_factorial(unittest.TestCase):
    def test_factresult(self):
        result = fact_func.fact(7)
        self.assertEqual(result, 5040)

if __name__ == '__main__':
    unittest.main()