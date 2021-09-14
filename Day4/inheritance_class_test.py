import unittest
from inheritance_class import Division

class Test_inheritance_class(unittest.TestCase):
    def test_division(self):
        divide = Division()  
        output = divide.Divide(10,20)
        self.assertEqual(output, 0.5)


if __name__ == '__main__':
    unittest.main()