import unittest
import print_instance_class

class Test_print(unittest.TestCase):
    def test_printing(self):
        elem = print_instance_class.Element('canada', 'tokyo', 321345)
        self.assertEqual(elem.name, 'canada')

if __name__ == '__main__':
    unittest.main()