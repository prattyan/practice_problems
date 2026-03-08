"""
Day 50: Strong Number

Question:
A strong number equals the sum of factorials of its digits (e.g. 145). Find them below 500.
"""

# Solution
from math import factorial

def is_strong(n):
    return n == sum(factorial(int(d)) for d in str(n))

print([n for n in range(1, 500) if is_strong(n)])
