"""
Day 143: Single Number (XOR)

Question:
Every element appears twice except one. Find it using XOR.
"""

# Solution
from functools import reduce
from operator import xor

a = [4, 1, 2, 1, 2]
print(reduce(xor, a))
