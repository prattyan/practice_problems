"""
Day 167: Operator Overloading: Vector

Question:
Create a Vector class that supports + and - using operator overloading.
"""

# Solution
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, o): return Vector(self.x + o.x, self.y + o.y)
    def __sub__(self, o): return Vector(self.x - o.x, self.y - o.y)
    def __repr__(self): return f"Vector({self.x}, {self.y})"

a, b = Vector(1, 2), Vector(3, 4)
print(a + b, a - b)
