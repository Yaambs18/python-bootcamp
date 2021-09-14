class Attendance:
    def __init__(self):
        self.st = [23, 34, 45, 6, 10, 56, 11]
        
    def check(self, roll):
        if roll in self.st:
            return "Present"
        else:
            return "Absent"

