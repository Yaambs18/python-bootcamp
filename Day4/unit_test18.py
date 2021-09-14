import unittest
from instance_count_class import Count

class Test_instance(unittest.TestCase):
    def test_count(self):
        g1 = Count()
        g2 = Count()
        g3 = Count()
        g4 = Count()
        g5 = Count()
        result = Count.counter
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
