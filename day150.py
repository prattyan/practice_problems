"""
Day 150: Rectangle Class

Question:
Create a Rectangle class with area and perimeter methods.
"""

# Solution
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

r = Rectangle(4, 6)
print(r.area(), r.perimeter())
