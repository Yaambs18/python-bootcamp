import unittest
from attendance_class import Attendance

class Test_runner(unittest.TestCase):
    def test_attendance(self):
        obj = Attendance()
        result = obj.check(23)
        self.assertEqual(result, "Present")

if __name__ == '__main__':
    unittest.main()