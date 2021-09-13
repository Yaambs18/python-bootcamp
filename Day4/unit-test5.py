import unittest
from unittest import result

import cylinder_class

class Test_volume_sa(unittest.TestCase):
    def test_volume(self):
        c = cylinder_class.Cylinder(2,3)
        result = c.volume()
        self.assertEqual(result, 56.52)

    def test_sa(self):
        c = cylinder_class.Cylinder(2,3)
        result = c.surface_area()
        self.assertEqual(result, 94.2)    

if __name__ == '__main__':
    unittest.main()
