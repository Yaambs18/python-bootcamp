import unittest
import perfect_num_func

class Test_perfect(unittest.TestCase):
    def test_perfecct_num(self):
        result = perfect_num_func.perfect_num(6)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()