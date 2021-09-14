import unittest
from animal_class import Dog

class Test_animal_class(unittest.TestCase):
    def test_dog(self):
        my_dog = Dog('Lab', 'Sammy', 'Nospots ')
        output = my_dog.bark()
        self.assertEqual(output, "Woof! My name is Sammy")


if __name__ == '__main__':
    unittest.main()