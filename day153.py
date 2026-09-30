"""
Day 153: Student Class with Average

Question:
Create a Student class that stores marks and returns the average.
"""

# Solution
class Student:
    def __init__(self, name, marks):
        self.name, self.marks = name, marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s = Student("Amit", [80, 90, 70])
print(s.name, round(s.average(), 2))
