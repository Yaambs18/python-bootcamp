from typing import Union
import unittest
import list_item_rev

class Test_rev(unittest.TestCase):
    def test_list_rev(self):
        l = ['abc', 'def', 'xyz']
        reverse = ['cba', 'fed', 'zyx']
        self.assertEqual(list_item_rev.rev(l), reverse)

if __name__ == '__main__':
    unittest.main()