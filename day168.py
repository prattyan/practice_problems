"""
Day 168: Fraction Class

Question:
Create a Fraction class with __str__ and addition (reduce to lowest terms).
"""

# Solution
from math import gcd

class Fraction:
    def __init__(self, n, d):
        g = gcd(n, d)
        self.n, self.d = n // g, d // g

    def __add__(self, o):
        return Fraction(self.n * o.d + o.n * self.d, self.d * o.d)

    def __str__(self):
        return f"{self.n}/{self.d}"

print(Fraction(1, 2) + Fraction(1, 3), Fraction(2, 4))
