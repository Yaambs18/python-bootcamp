import unittest
from book_class import Book

class Test_book_class(unittest.TestCase):
    def test_book(self):
        b = Book('Python Rock', 'Jose', 200)
        output = len(b)
        self.assertEqual(output, 200)


if __name__ == '__main__':
    unittest.main()