"""
Day 117: Combinations nCr

Question:
Compute nCr using a loop and list all k-combinations.
"""

# Solution
from itertools import combinations
from math import comb

print(comb(5, 2))
print(list(combinations([1, 2, 3, 4], 2)))
