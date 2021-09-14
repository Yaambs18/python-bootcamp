import unittest
from volume_class import Volume

class Test_vol(unittest.TestCase):
    def test_cube_vol(self):
        obj = Volume
        result = obj.cube(5)
        self.assertEqual(result, 125)

if __name__ == '__main__':
    unittest.main()